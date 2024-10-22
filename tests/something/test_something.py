import pytest
from src.generators.player_localization import PlayerLocalization


@pytest.mark.production
@pytest.mark.development
@pytest.mark.skip("[ISSUE-23442] Issue with network connection")
def test_equality():
    """
    In test we try to check that 1 is equal to 2
    """
    assert 1 == 2


@pytest.mark.development
@pytest.mark.parametrize(
    "first_value, second_value, result",
    [
        (1, 2, 3),
        (-1, -2, -3),
        (-1, 2, 1),
        ("b", -2, None),
        ("b", "b", None),
    ],
)
def test_calculator(first_value, second_value, result, calculate):
    """
    In test we check calculation for different values
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.parametrize(
    "status",
    [
        "ACTIVE",
        "BANNED",
        "DELETED",
        "INACTIVE",
    ],
)
def test_player_generator_with_different_status(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize(
    "delete_key",
    [
        "account_status",
        "balance",
        "localize",
        "avatar",
    ],
)
def test_delete_key(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_smth(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        "localize", PlayerLocalization("fr_FR").set_number(15)
    ).build()
    print(object_to_send)
