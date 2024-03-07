
from list_exo1 import filter_unique_elements


def test_filter_unique_elements_empty_list():
    assert filter_unique_elements([]) == []


def test_filter_unique_elements_no_duplicates():
    input_list = [1, 2, 3, 4, 5]
    assert filter_unique_elements(input_list) == input_list


def test_filter_unique_elements_with_duplicates():
    input_list = [1, 2, 2, 3, 4, 4, 5]
    assert filter_unique_elements(input_list) == [1, 3, 5]


def test_filter_unique_elements_strings():
    input_list = ["apple", "orange", "banana", "apple", "grape"]
    assert filter_unique_elements(input_list) == ["orange", "banana", "grape"]


def test_filter_unique_elements_mixed_types():
    input_list = [1, "apple", 2, "orange", 1, "banana", "apple"]
    assert filter_unique_elements(input_list) == [2, "orange", "banana"]
