from philh_myftp_biz.json import Dict
from philh_myftp_biz.file import JSON
from fastapi import APIRouter
from ... import User

router = APIRouter(
    prefix = '/Apps/Bookmark'
)

class BookmarkData(Dict[str]):

    def __init__(self, user:User) -> None:

        _json = JSON(user.Dir.child('Apps__Bookmark.json'))

        super().__init__(_json)

    def __getitem__(self, x:int) -> str:

        value = super().__getitem__(x)

        if value:
            return value
        else:
            return 'Type Here' 

@router.get("/read")
async def read_item( # pyright: ignore[reportRedeclaration]
    username: str,
    token: str
) -> None | dict[str, str]:
    """Read User Bookmark Data"""
    
    user = User(username)

    if user.checkAuth(token):

        data = BookmarkData(user)

        return {
            'Top': data[0],
            'Bot': data[1]
        } # pyright: ignore[reportReturnType]
     
@router.get("/save")
async def read_item(
    username: str,
    token: str,
    Top: str,
    Bot: str
) -> None:
    """Write User Bookmark Data"""
    
    user = User(username)

    if user.checkAuth(token):
        
        data = BookmarkData(user)

        data[0] = Top
        data[1] = Bot
