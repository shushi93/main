import pytest
from working import convert

def test_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_no_to():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

def test_error():
    with pytest.raises(ValueError):
        convert("9:61 AM to 8:310 PM")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("13:60 AM to 24:59 PM")
