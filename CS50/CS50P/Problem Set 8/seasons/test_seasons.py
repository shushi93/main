import pytest
from seasons import age

def test_year_ago():
    assert age("1999-01-01") == "Thirteen million, nine hundred ninety-eight thousand, two hundred forty"
