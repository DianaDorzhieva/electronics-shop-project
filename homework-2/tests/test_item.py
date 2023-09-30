"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

numb1 = Item("телефон",13000, 10)
def test_Item_calculate_total_price():
    assert numb1.calculate_total_price() == 130000

def test_Item_apply_discount():
    assert numb1.apply_discount() == 13000