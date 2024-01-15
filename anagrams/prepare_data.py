import importlib.resources
import logging
import pathlib
import pickle
from typing import Iterator, Mapping, List
from collections import Counter
import re

import pandas

from anagrams.config import SOURCE_TEXT
from anagrams.frozen_counter import FrozenCounter
from anagrams.name_storage import store_names_structure, NamesStructure
import anagrams.data

log = logging.getLogger(__name__)

def count_letters(text:str)->FrozenCounter:
    assert isinstance(text, str), f"Invalid input {text}"
    return FrozenCounter.from_str((re.sub(r"\s+", "", text.lower())))


def get_first_name_frames()->Iterator[pandas.DataFrame]:
    with importlib.resources.files("anagrams.data.names") as names:
        for filename in names.glob("*.txt"):
            yield pandas.read_csv(filename, header=None, names=["name", "sex", "code"])


def get_first_names()->pandas.DataFrame:
    df = pandas.concat(get_first_name_frames(), axis=0)
    return df[df.sex=="M"]["name"].str.lower().unique()

def get_last_names()->pandas.DataFrame:
    with importlib.resources.path(anagrams.data, "Names_2010Census.csv") as surnames_path:
        with surnames_path.open("r") as surnames_stream:
            data = pandas.read_csv(surnames_stream)

        return data["name"].str.lower().unique()


def get_names_dict(names:Iterator[str])->NamesStructure:
    result:Mapping[FrozenCounter:set[str]] = {}
    for i, name in enumerate(names):
        if i % 1000 == 0:
            log.info(f'Processing {name}')
        result.setdefault(count_letters(name).as_set(), set()).add(name)
    return result



def main():
    first_names = get_first_names()
    last_names = get_last_names()

    all_names = {x for x in set(first_names).union(set(last_names)) if isinstance(x,str)}

    names_dict: NamesStructure = get_names_dict(iter(all_names))
    log.info(f"Got {len(names_dict)} first_names")
    source_chars = count_letters(SOURCE_TEXT).as_set()
    filtered_names_dict = {k:v for k,v in names_dict.items() if k.issubset(source_chars)}
    store_names_structure(filtered_names_dict)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)


    main()