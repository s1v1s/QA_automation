from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)


def test_another():
    assert 1 == 1
