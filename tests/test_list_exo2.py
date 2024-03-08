
from list_exo2 import rotate_list


def test_rotate_list_empty_list():
    assert rotate_list([]) == []


def test_rotate_list_many_rotations():
    input_list = [1, 2, 3, 4, 5]
    assert rotate_list(input_list) == [4, 5, 1, 2, 3]


def test_rotate_list_one_rotation():
    input_list = [1, 2, 3, 4, 5]
    assert rotate_list(input_list) == [5, 1, 2, 3, 4]
