from pydantic import BaseModel


class BaseComplaint(BaseModel):
    """
    A class for represent a Complaint Base 
    
    It class has a minimun fields of Complaint Model
    
    Attributes
    ----------
    - title : str
        A string for title field.
    - description : str
        A description of complaint
    - photo_url : str
        The url where the image is saved
    - amount : float    
        Amount of complaint.
    """
    
    title: str
    description: str
    photo_url: str
    amount: float

class UserBase(BaseModel):
    """
    A class for represent a User Base
    
    It class has a minimum fields for UserModel
    
    Attributes
    ----------
    - email : str
        Email for the user    
    """
    email: str
