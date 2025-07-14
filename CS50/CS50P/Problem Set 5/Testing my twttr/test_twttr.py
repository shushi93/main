from twttr import shorten
import pytest
import sys

def main():
    test_normal_str()
    test_alphanumerical_str()
    test_special_chars()

def test_normal_str():
    assert shorten("twitter") == "twttr"
    assert shorten("name") == "nm"
    assert shorten("superduperlongstring") == "sprdprlngstrng"
    assert shorten("TESTTHIS") == "TSTTHS"

def test_alphanumerical_str():
    assert shorten("CS50") == "CS50"
    assert shorten("p@55w0rd") == "p@55w0rd"

def test_special_chars():
    for i in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]:
        assert shorten(i) == i
if __name__ == "__main__":
    main()
    sys.exit()
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE
