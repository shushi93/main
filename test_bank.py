from bank import value
import pytest

def test_normal_str():
    assert value("yes") == 100
    assert value("Hello") == 0
    assert value("H") == 20
    assert value("hElOO") == 20
    assert value("Hh") == 20

def test_numbers():
    for i in range(100000):
        i = str(i)
        assert value(i) == 100

def test_special_chars():
    for i in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]:
        assert value(i) == 100

def test_alphanumerical_str():
    assert value("CS50") == 100
    assert value("2") == 100
    assert value("h3llo") == 20
