"""
Model Package

Package with Complaint and User models. In this package too define the enums
roleType and State that we use in role user and state of complaint

Export:
-------
 - complaint : sqlAlchemy.Table
    A complaint table that represet a sqlAlchemy.Table. This class represents the table complait in database
 - user : sqlalchemy.Table
    A user table trat represent a sqlAlchemyTable. This class represents the table users in database
"""
from models.complaint import *
from models.user import *