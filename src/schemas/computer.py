from ipaddress import IPv4Address, IPv6Address

from pydantic import BaseModel, EmailStr
from pydantic.networks import IPvAnyAddress
from pydantic.types import FutureDate, List, PastDate
from pydantic_extra_types.payment import PaymentCardNumber

from src.enums.user_enums import Statuses
from src.schemas.physical import Physical

# from examples import computer


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPvAnyAddress = IPv4Address
    host_v6: IPvAnyAddress = IPv6Address
    detailed_info: DetailedInfo


# comp = Computer.model_validate(computer)
# print(comp.model_json_schema())
