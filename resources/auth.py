from fastapi import APIRouter
from managers.user import UserManager
from schemas.request.user import UserRegisterIn, UserLoginIn

router = APIRouter(tags=["Auth"])

@router.post("/register", status_code=201)
async def register(user_data: UserRegisterIn):
  """Register users endpoint
  
  This endpoint register a user in the app

  Args:
      user_data (UserRegisterIn): user_data is a instance of UserRegisterIn Schema

  Returns:
      String: Returns jwt token 
  """
  token = await UserManager.register(user_data.dict())
  return {
    "token": token
  }

@router.post("/login")
async def login(user_data: UserLoginIn):
  """Login Users

  Endpoint for users login

  Args:
    -  user_data (UserLoginIn): user_data with fields email and password. This user_data 
      corresponds a UserLoginIn schema

  Returns:
      string: Returns jwt token wich the user can navigate for anothers endpoints (if have permissions)
  """
  token = await UserManager.login(user_data.dict())
  return {"token": token}
