from fastapi import APIRouter
from typing import Literal
from __init__ import User

router = APIRouter(
    prefix = '/login'
)

@router.get("/change")
async def read_item(username:str, oldpassword:str, newpassword:str) -> None:
    """
    Change the Active Directory Pasword of a user
    """    
    user = User(username)

    if user.checkPass(oldpassword):
        user.setPass(newpassword)

@router.get("/create")
async def read_item(username:str, password:str) -> None | str:
    """
    Create an Active Directory User

    Returns an auth token
    """
    user = User(username)

    if not user.exists():
        user.setPass(password)
        return user.resetAuth()
    
@router.get("/check")
async def read_item(
    username: str,
    password: str,
    path: str
) -> dict[Literal['Valid', 'Alert', 'Token'], str|bool|None]:
    """
    Check if a User's Password is correct
    """
    user = User(username)

    response = {
        'Valid': False,
        'Alert': None,
        'Token': None
    }

    # Check if user exists
    if not user.exists():
        response['Alert'] = 'Username not found'

    # Check if password is correct
    elif user.checkPass(password):
        response['Valid'] = True
        response['Token'] = user.resetAuth()

    # Check if password is incorrect
    else:
        response['Alert'] = 'Password is incorrect'
 
    return response
    
@router.get("/auth")
async def read_item(
    username: str,
    token: str
) -> bool:
    """
    Check if a User's Auth Token is valid 
    """
    return User(username).checkAuth(token)