
from set_exo1 import find_intersection


def test_find_intersection():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    assert find_intersection(set1, set2) == {3, 4, 5}


def test_find_intersection_empty():
    set1 = {1, 2, 3, 4, 5}
    set2 = set()
    assert find_intersection(set1, set2) == set()


def test_find_intersection_duplicate():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 3, 4, 5, 5, 6, 7}
    assert find_intersection(set1, set2) == {3, 4, 5}
