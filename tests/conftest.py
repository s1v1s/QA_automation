from collections.abc import Callable
from random import randrange

import pytest

from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b


@pytest.fixture
def calculate() -> Callable[[int], int]:
    """
    Как это работает:
    calculate - fixture, которая при вызове возращает функцию
    _calculate - функция с входными данными
    """
    return _calculate


@pytest.fixture
def make_number():
    print("I`m getting number")
    number = randrange(1, 1000, 5)
    yield
    print(f"Number at home {number}")
