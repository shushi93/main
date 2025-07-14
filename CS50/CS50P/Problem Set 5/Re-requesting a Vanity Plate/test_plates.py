from plates import is_valid
import pytest

def test_len():
    assert is_valid("") == False
    assert is_valid("12345678") == False
    assert is_valid("CS50") == True
    assert is_valid("CSCSCS50") == False

def test_number_at_mid():
    assert is_valid("C55O") == False
    assert is_valid("1CS") == False
    assert is_valid("TH1H") == False
    assert is_valid("VANITY") == True
    assert is_valid("0") == False
    assert is_valid("CS05") == False

def test_invalid_char():
    assert is_valid("$$") == False
    assert is_valid("CS5()") == False
    assert is_valid("LOL") == True

def test_letterless():
    assert is_valid("1234") == False
    assert is_valid("!@#$") == False
    assert is_valid("!2#4%6") == False
    assert is_valid("VALID")== True
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE
