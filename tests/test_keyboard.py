"""Здесь надо написать тесты с использованием pytest для модуля Keyboard."""
import pytest
from src.keyboard import Keyboard, Mixinlog

def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    mx = Mixinlog()
    with pytest.raises(AttributeError) as e:
                         _= mx.language="rk"

