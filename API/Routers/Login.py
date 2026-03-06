from fastapi import APIRouter
from .. import User
from typing import Literal

router = APIRouter(
    prefix = '/login'
)

response: dict[Literal['Valid', 'Alert', 'Token'], str|bool|None] = {
    'Valid': False,
    'Alert': None,
    'Token': None
}

@router.get("/change")
async def read_item( # pyright: ignore[reportRedeclaration]
    username: str,
    oldpassword: str,
    newpassword: str
) -> None:
    """
    Change the Active Directory Password of a user
    """   

    user = User(username)

    if user.checkPass(oldpassword):
        user.setPass(newpassword)

@router.get("/create")
async def read_item( # pyright: ignore[reportRedeclaration]
    username: str,
    password: str
) -> None | str:
    """
    Create an Active Directory User

    Returns an auth token
    """

    user = User(username)

    if not user.exists:
        user.setPass(password)
        return user.resetAuth()
    
@router.get("/check")
async def read_item( # pyright: ignore[reportRedeclaration]
    username: str,
    password: str
):
    """
    Check if a User's Password is correct
    """
    
    user = User(username)

    r = response.copy()

    # Check if user exists
    if not user.exists:
        r['Alert'] = 'Username not found'

    # Check if password is correct
    elif user.checkPass(password):
        r['Valid'] = True
        r['Token'] = user.resetAuth()

    # Check if password is incorrect
    else:
        r['Alert'] = 'Password is incorrect'
 
    return r
    
@router.get("/auth")
async def read_item(
    username: str,
    token: str
):
    """
    Check if a User's Auth Token is valid 
    """

    user = User(username)

    r = response.copy()

    # Check if user exists
    if not user.exists:
        r['Alert'] = 'This page requires you to login'

    # Check if token is correct
    elif user.checkAuth(token):
        r['Valid'] = True

    # Check if token is incorrect
    else:
        r['Alert'] = 'Credentials Expired'
 
    return r
