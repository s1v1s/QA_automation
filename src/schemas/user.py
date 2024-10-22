from pydantic import BaseModel, field_validator

from src.enums.user_enums import Genders, StatusesLower, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: StatusesLower

    @field_validator("email")
    def check_that_dog_presented_in_email(cls, email: str) -> str:
        if "@" in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
