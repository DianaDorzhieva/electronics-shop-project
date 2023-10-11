"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest
from src.item import Item
from src.phone import Phone

def test__add__():
    it = Item("смартфон", 15000, 15)
    ph = Phone("Суперсмартфон", 13000, 16, 2)
    assert it + ph == 31
    with pytest.raises(ValueError) as e: _= ph + 20
    with pytest.raises(ValueError) as e: _= it + 20
    with pytest.raises(ValueError) as e: _= Phone("Суперсмартфон", 13000, 16, 0)
