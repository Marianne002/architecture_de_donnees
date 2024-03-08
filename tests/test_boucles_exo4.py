
from boucles_exo4 import decode_message


def test_decode_message_simple():
    assert decode_message("72 101 108 108 111") == "Hello"


def test_decode_message_empty_input():
    assert decode_message("") == ""


def test_decode_message_with_spaces():
    assert decode_message("65 66 67 32 68 69 70") == "ABC DEF"


def test_decode_message_special_characters():
    assert decode_message("33 64 35 36 37") == "!@#$%"


def test_decode_message_mixed():
    assert decode_message("97 98 99 65 66 67") == "abcABC"
