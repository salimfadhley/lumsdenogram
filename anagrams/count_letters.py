from collections import Counter
from typing import Tuple

CountLettersResultStructure = Tuple[Tuple[str,int]]

def cl(inp:str)->CountLettersResultStructure:
    c = Counter(inp.lower().replace(" ", ""))
    return tuple((char, count) for (char, count) in sorted(c.items()))


class InvalidCompliment(ValueError):
    pass

def compliment_count(a:CountLettersResultStructure, b:CountLettersResultStructure)->CountLettersResultStructure:
    a_dict = dict(a)
    b_dict = dict(b)
    result_dict = {}
    for char in set(a_dict.keys()).union(set(b_dict.keys())):
        r = a_dict.get(char, 0) - b_dict.get(char, 0)
        if r < 0:
            raise InvalidCompliment(f"Invalid value for {char}:{r}")
        result_dict[char] = r
    return tuple(x for x in sorted(result_dict.items()) if x[1] != 0)

def char_subset(big:CountLettersResultStructure, small:CountLettersResultStructure)->bool:
    try:
        compliment_count(big,small)
    except InvalidCompliment:
        return False
    return True