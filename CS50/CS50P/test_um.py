import pytest
from um import count

def test():
    assert count("um") == 1

def test_word():
    assert count("sum lum rum") == 0

def test_case():
    assert count("Um") == 1
