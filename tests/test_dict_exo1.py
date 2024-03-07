
from dict_exo1 import students_above_15


def test_students_above_15():
    students = {
        "Chungha": 18,
        "Bob": 8,
        "Charlie": 10,
        "Hwa": 20,
        "Eve": 14,
    }
    expected = {
        "Chungha": 18,
        "Hwa": 20,
    }
    assert students_above_15(students) == expected


def test_students_above_15_empty():
    students = {}
    expected = {}
    assert students_above_15(students) == expected
