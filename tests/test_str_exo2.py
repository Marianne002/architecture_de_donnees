
from str_exo2 import (
    extract_word,
    extract_word_negative_index,
    extract_word_slicing,
    reverse_string
)


def test_extract_word():
    sentence = "Python est un langage de programmation puissant"
    assert extract_word(sentence) == "Python"


def test_extract_word_negative_index():
    assert extract_word_negative_index("Facile à apprendre") == "apprendre"


def test_extract_word_slicing():
    sentence = "Python est un langage de programmation"
    assert extract_word_slicing(sentence) == ['langage', 'de', 'programmation']


def test_reverse_string():
    sentence = "Python est un langage"
    assert reverse_string(sentence) == "egagnal nu tse nohtyP"
