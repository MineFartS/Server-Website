from typing import Literal
from fastapi import APIRouter, UploadFile
from fastapi.responses import RedirectResponse
from __init__ import User

router = APIRouter(
    prefix = '/Apps/Videos'
)

detailsHint = dict[Literal['ID', 'Title', 'Description', 'Timestamp', 'Uploader', 'Views', 'Visibility']]

def VideoDetails(
    id: str
):# -> detailsHint:
    """
    Get a philh_myftp_biz.json.new object with the video details
    """
    from philh_myftp_biz.json import new
    from philh_myftp_biz.file import json
    from philh_myftp_biz.pc import Path

    return new(json(
        path = Path(f'E:/Website/Resources/Apps/Videos/files/{id}')
    ))

@router.post('/Apps/Videos/Upload')
async def upload(
    username: str,
    token: str,
    Title: str,
    Description: str,
    Visibility: str,
    Video: UploadFile,
    Thumbnail: UploadFile
):
    """
    Upload a video

    Thumbnail will be automatically generated if not given
    """
    from __init__ import receiveFile
    from philh_myftp_biz.text import random
    from philh_myftp_biz.time import now

    user = User(username)

    if user.checkAuth(token):

        id = random(10)

        vid = VideoDetails(id)

        receiveFile(Video).move()
        
        if len(Thumbnail.filename) > 0:
            Thumbnail = receiveFile(Thumbnail)
        else:
            Thumbnail = None

        vid["id"] = id,
        vid["Title"] = Title,
        vid["Description"] = Description,
        vid["Timestamp"] = now().unix,
        vid["Uploader"] = username,
        vid["Views"] = 0
        vid["Visibility"] = Visibility
    
        return f"https://philh.myftp.biz/Apps/Videos/Player?id={id}"

@router.get('/Apps/Videos/List')
async def read_item(
    username: str = None,
    token: str = None
) -> list[dict]:
    """
    List All Videos

    If Username and Auth Token are valid, then the user's private videos will be included
    """
    from philh_myftp_biz.pc import Path
    from __init__ import root

    if username:
        user = User(username)
        show_private = user.checkAuth(token)
    else:
        show_private = False

    items = []

    files = root.child('/Apps/Videos/files')
    
    for p in Path(files).children():
        if p.isdir():

            details = VideoDetails(p.name())
            
            if details['Visibility'] == 'Public':
                visible = True
            elif show_private:
                visible = (details['Uploader'] == username)
            else:
                visible = False

            if visible:
                items.append(details.read())

    return sorted(
        iterable = items,
        key = lambda x: x['Timestamp']
    )

@router.get('/Apps/Videos/Channels')
async def read_item() -> list[str]:
    """
    List all Channels
    """
    from __init__ import root

    channels = []

    dir = root.child('/Apps/Videos/files')
    
    for p in dir.children():
        if p.isdir():
            
            details = VideoDetails(p.name())
            
            if not details['Uploader'] in channels:
                channels += [details['Uploader']]

    return sorted(channels)

@router.get('/Apps/Videos/View')
async def read_item(
    id: str,
    c: bool = True
) -> detailsHint:
    """
    Get the details of a video

    If c, then add 1 view
    """

    details = VideoDetails(id)

    if c:
        details['Views'] += 1

    return details

@router.get('/Apps/Videos/Delete')
async def upload(
    id: str,
    username: str,
    auth: str
) -> None:
    """
    Delete a video
    """
    
    VideoDetails(id).var.path.parent().delete()

@router.post('/Apps/Videos/Modify')
async def upload(
    username: str,
    token: str,
    Title: str,
    Description: str,
    Visibility: str,
    Thumbnail: UploadFile,
    ID: str
) -> None | RedirectResponse:
    """
    Modify an existing Video
    """
    from __init__ import receiveFile

    user = User(username)

    if user.checkAuth(token):

        details = VideoDetails(ID)

        if len(Thumbnail.filename) > 0:
            receiveFile(Thumbnail).move()

        details['Title'] = Title
        details['Description'] = Description
        details['Visibility'] = Visibility

        return RedirectResponse(f"https://philh.myftp.biz/Apps/Videos/Player?id={id}")