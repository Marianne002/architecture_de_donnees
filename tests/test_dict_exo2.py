
from dict_exo2 import out_of_stock


def test_out_of_stock_empty():
    products = {}
    assert out_of_stock(products) == []


def test_out_of_stock():
    products = {
        1: {"name": "apple", "price": 1.5, "quantity": 0},
        2: {"name": "banana", "price": 0.5, "quantity": 0},
        3: {"name": "cherry", "price": 2.5, "quantity": 1},
        4: {"name": "date", "price": 3.5, "quantity": 0},
    }
    expected = [
        {"id": 4, "price": 3.5, "name": "date"},
        {"id": 1, "price": 1.5, "name": "apple"},
        {"id": 2, "price": 0.5, "name": "banana"},
    ]
    assert out_of_stock(products) == expected
