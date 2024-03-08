
from set_exo2 import find_symmetric_difference


def test_find_symmetric_difference_empty():
    set1 = {1, 2, 3, 4, 5}
    set2 = set()
    assert find_symmetric_difference(set1, set2) == {1, 2, 3, 4, 5}


def test_find_symmetric_difference():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    assert find_symmetric_difference(set1, set2) == {1, 2, 6, 7}


def test_find_symmetric_difference_mixed_data_types():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7, "a", "b"}
    assert find_symmetric_difference(set1, set2) == {1, 2, 6, 7, "a", "b"}
