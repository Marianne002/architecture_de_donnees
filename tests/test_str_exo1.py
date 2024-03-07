
from str_exo1 import count_upp_low


def test_count_all_uppers():
    assert count_upp_low("FOOD") == "4 majuscules et 0 minuscules"


def test_count_all_lowers():
    assert count_upp_low("food") == "0 majuscules et 4 minuscules"


def test_count_mixed_uppers_lowers():
    assert count_upp_low("Food") == "1 majuscules et 3 minuscules"
