import pathlib
import pickle
from typing import Type, Mapping, Tuple, FrozenSet

from anagrams.frozen_counter import FrozenCounter

NameKey:Type = FrozenSet[Tuple[str,int]]
NamesStructure:Type = Mapping[NameKey,set[str]]

NAMES_STORAGE_FILE_NAME:str = "processed_names.pickle"

def get_storage_file()->pathlib.Path:
    return pathlib.Path(NAMES_STORAGE_FILE_NAME)

def get_names_structure()->NamesStructure:
    with get_storage_file().open("rb") as read_file:
        return pickle.load(read_file)

def store_names_structure(data:NamesStructure)->None:
    with get_storage_file().open("wb") as write_file:
        pickle.dump(data, write_file)
