
from tuples_exo2 import reverse_tuples


def test_reverse_tuples_empty_list():
    assert reverse_tuples([]) == []


def test_reverse_tuples_single_tuple():
    input_list = [(1, 2, 3)]
    assert reverse_tuples(input_list) == [(3, 2, 1)]


def test_reverse_tuples_multiple_tuples():
    input_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9)]
    assert reverse_tuples(input_list) == [(3, 2, 1), (5, 4), (9, 8, 7, 6)]
