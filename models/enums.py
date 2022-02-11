import enum


class RoleType(enum.Enum):
    aprover = "aprover"
    complainer = "complainer"
    admin = "admin"


class State(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Reject"
