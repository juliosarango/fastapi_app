from schemas.base import UserBase
from models.enums import RoleType
from typing import Optional


class UserOut(UserBase):
    id: int
    first_name: str
    last_name: str
    phone: Optional[str]
    role: RoleType
    iban: Optional[str]

