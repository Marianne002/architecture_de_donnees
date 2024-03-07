from tuples_exo1 import tuple_max


def test_tuple_max_empty_list():
    assert tuple_max([]) is None


def test_tuple_max_single_tuple():
    input_list = [(1, 2, 3)]
    assert tuple_max(input_list) == (1, 2, 3)


def test_tuple_max_multiple_tuples():
    input_list = [(1, 2, 3), (4, 5), (6, 7, 8, 9)]
    assert tuple_max(input_list) == (6, 7, 8, 9)
