import pytest

from anagrams.count_letters import cl, compliment_count, char_subset


def test_count_letters0():
    assert cl("a") == (
        (("a", 1),)
    )

def test_count_letters1():
    assert cl("A") == (
        (("a", 1),)
    )


def test_count_letters2():
    assert cl("aA") == (
        (("a", 2),)
    )

def test_count_letters3():
    assert cl("aAbbb") == (
        (("a", 2),("b", 3),)
    )

def test_count_letters4():
    assert cl("bbba") == (
        (("a", 1),("b", 3),)
    )

def test_count_letters5():
    assert cl("bbb a") == (
        (("a", 1),("b", 3),)
    )

def test_compliment0():
    assert compliment_count(
        cl("a"),
        cl("a")
    ) == cl("")

def test_compliment1():
    with pytest.raises(ValueError):
        compliment_count(
            cl("a"),
            cl("b")
        )

def test_compliment2():
    assert compliment_count(
        cl("abc"),
        cl("cba")
    ) == cl("")

def test_char_subset0():
    assert char_subset(big=cl("aaa"), small=cl("a"))

def test_char_subset1():
    assert not char_subset(big=cl("aaa"), small=cl("aaaa"))