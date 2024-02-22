# import itertools
# from collections import Counter
# from typing import Optional, Iterable, Iterator, Tuple, FrozenSet
#
#
# class FrozenCounter:
#     def __init__(self, counter:Counter):
#         self._counter = counter
#
#     @classmethod
#     def from_str(cls, text:str)->"FrozenCounter":
#         return cls(Counter(text))
#
#     def __getitem__(self, key):
#         return self._counter.get(key, 0)
#
#     def __iter__(self):
#         return iter(self.items())
#
#     def __len__(self):
#         return len(self._counter)
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self._counter})'
#
#     def __eq__(self, other):
#         assert isinstance(other, FrozenCounter), f"other is not the right type: {other=} {type(other)=}."
#         return list(self.items()) == list(other.items())
#
#     def __hash__(self)->int:
#         return hash(self.items())
#
#     def keys(self)->Iterator[str]:
#         yield from sorted(self._counter.keys())
#
#     def items(self)->Iterator[Tuple[str,int]]:
#         for k in self.keys():
#             v = self._counter[k]
#             if v > 0:
#                 yield (k, v)
#
#
#     def compliment(self, otherls:"FrozenCounter")->"FrozenCounter":
#         new_counter = Counter()
#
#         iterators = [self.items(), ((k,v*-1) for k,v in other.items())]
#
#         for k,v in itertools.chain(*iterators):
#             new_counter[k] += v
#
#         if not all(a >= 0 for a in new_counter.values()):
#             raise ValueError(f"Invalid counter. Some values are negative: {new_counter}")
#
#         return FrozenCounter(new_counter)
#
#
#
#
#     def is_subset_of(self, other:"FrozenCounter")->bool:
#         result = {k:other[k] >= v for k,v in self.items()}
#         return all(result.values())
#
#     def as_set(self)->FrozenSet[Tuple[str,int]]:
#         return frozenset(self.items())
