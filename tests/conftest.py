"""
scope:
function - (по умолчанию) повторное выполнение fixture при повторном вызове,
session - выполнение fixture единожды и затем использование кэшированного результата в рамках всего теста
Замысел - повышение производительности/скорости исполнения тестов за счёт исключения повторяющихся действий
autouse:
True - fixture будет исполняться для каждого теста без дополнительного указания
"""

from random import randrange
from collections.abc import Callable
import pytest


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a: int, b: int) -> int:
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
