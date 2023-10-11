"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


def test_Item_calculate_total_price():
    numb1 = Item("телефон", 13000, 10)
    assert numb1.calculate_total_price() == 130000

def test_Item_apply_discount():
    numb10 = Item("телефон", 13000, 10)
    numb10.pay_rate = 0.5
    numb10.apply_discount()
    assert numb10.price == 6500

def test_Item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_Item_len_name():
    numb2 = Item("телефон", 13000, 10)
    numb2.name = 'СуперСмартфон'
    assert numb2.name == 'СуперСмарт'

def test__str__():
    numb4 = Item('телефон', 13000, 10)
    assert str(numb4) == 'телефон'

def test__repr__():
    numb5 = Item('Смартфон', 10000, 20)
    assert repr(numb5) == "Item('Смартфон', 10000, 20)"

def test__add__():
    it = Item("смартфон", 15000, 15)
    ph = Phone("Суперсмартфон", 13000, 16, 2)
    assert it + ph == 31
    with pytest.raises(ValueError) as e: _= ph + 20
    with pytest.raises(ValueError) as e: _= it + 20
    with pytest.raises(ValueError) as e: _= Phone("Суперсмартфон", 13000, 16, 0)

