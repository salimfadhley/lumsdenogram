import itertools
import logging

from anagrams.config import SOURCE_TEXT
from anagrams.count_letters import cl, CountLettersResultStructure, compliment_count, InvalidCompliment
from anagrams.name_storage import get_names_structure, NamesStructure

log = logging.getLogger(__name__)

def main():
    source_chars:CountLettersResultStructure = cl(SOURCE_TEXT)
    names_struct:NamesStructure = get_names_structure()

    with open("anagram_names.txt", "w") as output_file:
        for k,names in names_struct.items():
            try:
                k_complement = compliment_count(source_chars,k)
            except InvalidCompliment as ve:
                # log.info(f"No complement of {next(iter(names))}")
                continue

            if k_complement in names_struct:
                last_names = names_struct[k_complement]
                for name in names:
                    for last_name in last_names:
                        full_name = f"{name} {last_name}"
                        log.info(full_name)
                output_file.write(f"{full_name}\n")





if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()