from fastapi import APIRouter
from Website_API import User
from typing import Literal

router = APIRouter(
    prefix = '/App/Bookmark'
)

def BookmarkData(
    user: User
) -> dict[Literal['Top', 'Bottom'], str]:
    """
    Get a philh_myftp_biz.file.json object with the User's data file
    """
    from philh_myftp_biz.file import JSON
    from philh_myftp_biz.json import Dict

    return Dict(JSON(
        path = user.Dir.child('BookmarkApp.json'),
        default = {'Top':'', 'Bottom':''}
    ))

@router.get("/Apps/Bookmark/read")
async def read_item(
    username: str,
    token: str
) -> None | dict[Literal['Top', 'Bottom'], str]:
    """
    Read User Bookmark Data
    """
    
    user = User(username)

    if user.checkAuth(token):
        
        data = BookmarkData(user)

        return data.read()
     
@router.get("/Apps/Bookmark/write")
async def read_item(
    username: str,
    token: str,
    Top: str,
    Bottom: str
) -> None:
    """
    Write User Bookmark Data
    """
    
    user = User(username)

    if user.checkAuth(token):
        
        data = BookmarkData(user)

        data['Top'] = Top
        data['Bottom'] = Bottom
