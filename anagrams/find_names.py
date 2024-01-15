import itertools
import logging

from anagrams.config import SOURCE_TEXT
from anagrams.name_storage import get_names_structure, NamesStructure, NameKey
from anagrams.prepare_data import count_letters

log = logging.getLogger(__name__)

def compliment(big:NameKey, small:NameKey)->NameKey:
    result = {}
    all_keys = itertools.chain([big, ((k,v*-1) for k,v in small)])
    for k,v in all_keys:
        result[k] = result.setdefault(k,0) + v
    return frozenset((k,result[k]) for k in result.keys() if result[k] > 0)

def main():
    source_chars = count_letters(SOURCE_TEXT).as_set()
    names_struct:NamesStructure = get_names_structure()

    for k,names in names_struct.items():
        try:
            k_complement = compliment(source_chars,k)
        except ValueError as ve:
            # log.info(f"No complement of {next(iter(names))}")
            continue
        last_names = names_struct[k_complement]
        for name in names:
            for last_name in last_names:
                log.info(f"{name} {last_name}")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()