import pytest


@pytest.mark.production
@pytest.mark.development
@pytest.mark.skip("[ISSUE-23442] Issue with network connection")
def test_something(get_number):
    assert 1 == 1
    print(get_number)


def test_calculation_both_negative(calculate):
    print(calculate(-1, -2))


def test_calculation_one_negative(calculate):
    print(calculate(1, -2))


def test_calculation_one_positive(calculate):
    print(calculate(1, 2))


def test_calculation_one_char(calculate):
    print(calculate(1, "2"))


def test_calculation_two_chars(calculate):
    print(calculate("1", "2"))


@pytest.mark.development
@pytest.mark.parametrize(
    "first_value, second_value, result",
    [(1, 2, 3), (-1, -2, -3), (-1, 2, 1), ("b", -2, None), ("b", "b", None)],
)
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
