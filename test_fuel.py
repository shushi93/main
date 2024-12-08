from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("5/6") == 83
    assert convert("1/3") == 33
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(46) == "46%"

def test_gauge_float():
    assert gauge(0.1) == "E"
    assert gauge(99.9) == "F"
    assert gauge(50) == "50%"
