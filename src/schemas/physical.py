from pydantic import UUID4, BaseModel, HttpUrl
from pydantic_extra_types.color import Color


class Physical(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4
