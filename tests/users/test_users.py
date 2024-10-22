from examples import computer
from src.baseclasses.response import Response
from src.schemas.computer import Computer
from src.schemas.user import User


def test_getting_users_list(get_users, calculate, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(calculate)
    print(calculate(1, 1))
    print(make_number)


def test_pydantic_object():
    comp = Computer.model_validate(computer)
    print(comp.detailed_info.physical.photo.host)
    print(comp.detailed_info.physical.color.as_rgb)
