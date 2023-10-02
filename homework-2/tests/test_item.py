"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_Item_calculate_total_price():
    numb1 = Item("телефон", 13000, 10)
    assert numb1.calculate_total_price() == 130000

def test_Item_apply_discount():
    numb1 = Item("телефон", 13000, 10)
    Item.pay_rate = 0.5
    assert numb1.price == 6500

def test_Item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_Item_len_name():
    numb1 = Item("телефон", 13000, 10)
    numb1.name = 'СуперСмартфон'
    assert numb1.name == 'СуперСмарт'
