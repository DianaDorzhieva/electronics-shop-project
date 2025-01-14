"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_Item_calculate_total_price():
    numb1 = Item("телефон", 13000, 10)
    assert numb1.calculate_total_price() == 130000

#def test_Item_apply_discount():
    numb2 = Item("телефон", 13000, 10)
    Item.pay_rate = 0.5
    numb2.apply_discount()
    assert numb2.price == 6500