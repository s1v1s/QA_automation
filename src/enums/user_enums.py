from enum import Enum


class Genders(Enum):
    FEMALE = "female"
    MALE = "male"


class Statuses(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn`t contain @"
