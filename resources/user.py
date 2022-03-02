from fastapi import APIRouter, dependencies, Depends
from managers.auth import oauth2_scheme, is_admin
from managers.user import UserManager
from typing import Optional
from models.enums import RoleType
from schemas.response.user import UserOut
from typing import List


router = APIRouter(tags=["Users"])


@router.get(path="/user", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], response_model=UserOut)
async def get_user(email: str):        
    """Get user
    
    Endpoint for get a user by email. The user that execute the endpoint must have admin_role.

    Args:
        email (str): Email of user

    Returns:
        UserOut: UserOut schema
    """
    return await UserManager.get_user_by_email(email)    

@router.get(path="/users", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], response_model=List[UserOut])
async def get_users():    
    """Get all Users
    
    This endpoint get all users from database. The user that execute the endpoint must have admin_role.

    Returns:
        UserOut: A list of UserOut schema
    """        
    return await UserManager.get_all_users()

@router.put("/users/{user_id}/make-admin", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def change_admin(user_id: int):
    """Chance admin profile
    
    This endpoint allows to change a role to admin-role. The user that execute the endpoint must have admin_role.

    Args:
        user_id (int): user Id
    """
    await UserManager.change_role(RoleType.admin, user_id)

@router.put("/users/{user_id}/make-approver", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def change_approver(user_id: int):
    """Chance approver profile
    
    This endpoint allows to change a role to approver-role. The user that execute the endpoint must have admin_role.

    Args:
        user_id (int): user Id
    """
    await UserManager.change_role(RoleType.aprover, user_id)