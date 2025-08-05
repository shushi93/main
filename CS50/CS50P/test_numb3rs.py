from numb3rs import validate
import pytest

def test_bytes():
    assert validate("155.155.155.155.155") == False
    assert validate("155.155.155.155.155.155") == False
def test_rest_not_in_range():
    assert validate("1.256.356.1000") == False
def test_all_not_in_range():
    assert validate("278.678.678.678") == False
