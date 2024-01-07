import importlib.resources
from pathlib import Path
from typing import Iterator

import pandas


def get_name_frames()->Iterator[pandas.DataFrame]:
    with importlib.resources.files("anagrams.data.names") as names:
        for filename in names.glob("*.txt"):
            yield pandas.read_csv(filename, header=None, names=["name", "sex", "code"])


def get_first_names()->pandas.DataFrame:
    df = pandas.concat(get_name_frames(), axis=0)
    return df[df.sex=="M"]["name"].str.lower().unique()


def main(source_text="nicolalumsden"):
    names = get_first_names()
    source_chars = set(source_text)

    for name in names:
        name_chars = set(name)
        if name_chars.issubset(source_chars):
            remainder_chars = source_chars - name_chars
            for name2 in names:
                name2_chars = set(name2)
                if name2_chars == remainder_chars:
                    print(f"{name} {name2}")




if __name__ == "__main__":
    main()