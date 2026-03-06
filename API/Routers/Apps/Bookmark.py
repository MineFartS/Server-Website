from philh_myftp_biz.array import List
from philh_myftp_biz.file import JSON
from fastapi import APIRouter
from ... import User

router = APIRouter(
    prefix = '/Apps/Bookmark'
)

def UserData(
    user: User
):
    """
    Get a philh_myftp_biz.file.json object with the User's data file
    """

    return List(JSON(
        path = user.Dir.child('Apps__Bookmark.json'),
        default = ['Type Here', 'Type Here']
    ))

@router.get("/read")
async def read_item( # pyright: ignore[reportRedeclaration]
    username: str,
    token: str
) -> None | dict[str, str]:
    """
    Read User Bookmark Data
    """
    
    user = User(username)

    if user.checkAuth(token):
        
        data = UserData(user).read()

        return {
            'Top': data[0],
            'Bottom': data[1]
        }
     
@router.get("/save")
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
        
        data = UserData(user)

        data.save([Top, Bottom])
