from enum import Enum

from src.enums.pyenum import PyEnum


class Genders(Enum):
    FEMALE = "female"
    MALE = "male"


class StatusesLower(Enum):
    active = "active"
    banned = "banned"
    deleted = "deleted"
    inactive = "inactive"


class Statuses(PyEnum):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn`t contain @"
