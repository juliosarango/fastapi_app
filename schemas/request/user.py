from schemas.base import UserBase

class UserRegisterIn(UserBase):
    """ UserRegistrerIn class
    
    This class represents the schema of user with data of user with the endpoint /register
    
    Attributes
    ----------
    - email : str
        Inherith from UserBase class. This fiel is required
    - password: str
        Password for the new user. This fiel is required
    - first_name: str
        Firts name of the user. This fiel is required
    - last_name: str
        Last name of the user. This fiel is required
    - phone: str
        Phone of the user. This fiel is required
    - iban: str
        Iban for the user. This fiel is required
    """
    password: str
    first_name: str
    last_name: str
    phone: str
    iban: str


class UserLoginIn(UserBase):
    """
    UserLogin class
    
    This class has the field for user login
    
    Attributes
    ----------
    - email: str
        Inherith from UserBase class. This fiel is required
    - password: str
        The password for user. This fiel is required
    """
    password: str
