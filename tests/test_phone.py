"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest
from src.item import Item
from src.phone import Phone

def test__add__():
    it = Item("смартфон", 15000, 15)
    ph = Phone("Суперсмартфон", 13000, 16, 2)
    assert it + ph == 31
    assert it + 20 == None
    assert ph + 20 == None
