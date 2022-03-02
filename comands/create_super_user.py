""" CreateSuperUser Command

This script allows create a user with admin_role. To execute this script, the 
user has provide the follow parameters:

Parameters
----------
- first_name: str
    Firts name of the user that will we create    
- last_name: str
    Last name of the user that will we create    
- email: str
    Email of the user that will we create    
-phone: str
    Phone of the user that will we create        
- iban: str
    Iban of the user that will we create        
- pw: str    
    Password of the user that will we create    

"""
import click
from managers.user import UserManager
from models import RoleType
from config.db import database

import asyncclick as click

@click.command()
@click.option("-f", "--first_name", type= str, required=True)
@click.option("-l", "--last_name", type= str, required=True)
@click.option("-e", "--email", type= str, required=True)
@click.option("-p", "--phone", type= str, required=True)
@click.option("-i", "--iban", type= str, required=True)
@click.option("-pw", "--password", type= str, required=True)

async def create_user(first_name, last_name, email, phone, iban, password):
    """Create admi user command
    
    Command for create a admin user in the app

    Args:
        first_name (str): First name 
        last_name (str): Last name
        email (str): Email
        phone (str): Phone 
        iban (str): Iban 
        password (str): Password
    """
    user_data = {
        "first_name": first_name, "last_name":last_name, "email": email,
        "phone": phone, "iban": iban, "password": password, "role": RoleType.admin
    }

    await database.connect()
    await UserManager.register(user_data)
    await database.disconnect()

if __name__ == "__main__":
    create_user(_anyio_backend="asyncio")