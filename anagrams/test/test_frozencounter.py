from anagrams.frozen_counter import FrozenCounter
from anagrams.prepare_data import count_letters

def test_types0():
    result = count_letters("cba")
    assert isinstance(result, FrozenCounter)

def test_frozencounter_0():
    assert dict(count_letters("a").items()) == {"a":1}

def test_frozencounter_1():
    assert dict(count_letters("A").items()) == {"a":1}

def test_frozencounter_2():
    assert dict(count_letters("Aa").items()) == {"a":2}


def test_frozencounter_3():
    assert dict(count_letters("AaB").items()) == {"a":2, "b":1}

def test_frozencounter_4():
    assert dict(count_letters("AaBbb ").items()) == {"a":2, "b":3}

def test_frozencounter_5():
    assert count_letters("AaBbCc").is_subset_of(count_letters("AaBbCcDd"))

def test_frozencounter_6():
    assert not count_letters("A").is_subset_of(count_letters(""))

def test_frozencounter_7():
    assert count_letters("").is_subset_of(count_letters(""))

def test_frozencounter_8():
    assert count_letters("abcd") == count_letters("dcba")

def test_frozencounter_9():
    assert count_letters("abcd") == count_letters("DCBA")

def test_frozenset_compliment_0():
    assert count_letters("").compliment(count_letters(""))==count_letters("")

def test_frozenset_compliment_1():
    assert count_letters("aa").compliment(count_letters(""))==count_letters("aa")

def test_frozenset_compliment_2():
    assert count_letters("aa").compliment(count_letters("a"))==count_letters("a")

def test_frozenset_compliment_3():
    assert count_letters("aabbcc").compliment(count_letters("a"))==count_letters("abbcc")

def test_frozenset_hash0():
    assert hash(count_letters(""))==hash(count_letters(""))

def test_frozenset_hash1():
    assert hash(count_letters("a"))==hash(count_letters("A"))

def test_frozenset_hash1():
    assert hash(count_letters("ab"))==hash(count_letters("BA"))

def test_frozenset_keys0():
    assert "".join(count_letters("cba").keys()) == "abc"

def test_frozenset_items0():
    assert [a for a in count_letters("cba").items()] == [("a",1), ("b",1), ("c",1)]


def test_frozenset_items0():
    assert list(count_letters("abc").compliment(count_letters("abc")).items() ) == []


