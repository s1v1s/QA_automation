import pytest
import requests
from configuration import SERVICE_URL

"""
Параметр scope:
function - (по умолчанию) повторное выполнение fixture при повторном вызове,
session - выполнение fixture единожды и затем использование кэшированного результата в рамках всего теста
Замысел - повышение производительности/скорости исполнения тестов за счёт исключения повторяющихся действий

Параметр autouse:
True - fixture будет исполняться для каждого теста без дополнительного указания
"""


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL)
    return response
