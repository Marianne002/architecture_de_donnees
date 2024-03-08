
from boucles_exo3 import higher_number


def test_higher_number_a():
    assert higher_number(5, 3, 1) == 5


def test_higher_number_b():
    assert higher_number(2, 8, 4) == 8


def test_higher_number_c():
    assert higher_number(6, 2, 9) == 9


def test_higher_number_equal():
    assert higher_number(4, 4, 4) == 4
