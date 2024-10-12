from pydantic import BaseModel, Field  # , field_validator, ValidationInfo


class Post(BaseModel):
    id: int = Field(le=2)
    title: str
    # name: str = Field(alias="_name")

    # Этот валидатор заменяется одной строкой id: int = Field(le=2)
    # Старый validator
    # Новый filed_validator
    # @field_validator("id")
    # def check_that_id_is_less_than_two(cls, v: int, info: ValidationInfo) -> int:
    #     if v > 2:
    #         raise ValueError("id is not less than 2")
    #     else:
    #         return v


# Старый Post.parse_obj
# Новый Post.model_validate
# Post.model_validate_json
# {"id": 1, "title": "Post 1"}
