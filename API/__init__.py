from philh_myftp_biz.file import temp, ZIP, TXT
from http.cookiejar import MozillaCookieJar
from philh_myftp_biz.modules import Module
from philh_myftp_biz.web import download
from browser_cookie3 import firefox
from philh_myftp_biz.pc import Path
from philh_myftp_biz.db import Ring
from fastapi import UploadFile

# ================================================================================================================

this = Module('E:/Website')
Users = Module('E:/Users')

root = this.dir.child('Root')

tokenRing = Ring('AuthTokens')

PIDstore = TXT(this.dir.child('/API/__pycache__/PID.txt'))

# ================================================================================================================

async def receiveFile(stream: 'UploadFile') -> Path:
    from philh_myftp_biz.file import temp
    from aiofiles import open

    path = temp(
        name = 'UploadedFile',
        ext = stream.filename[stream.filename.rfind('.')+1:]
    )   

    contents = await stream.read()

    async with open(str(path), 'wb') as f:
        await f.write(contents)

    return path

# ================================================================================================================

class User:

    def __init__(self, username:str):
        
        self.username = username
        self.Dir = Path(f'E:/Users/philh/{username}/__AppData__/')

        self.__token = tokenRing.Key(username)

    def checkPass(self, password:str):
        return Users.run(
            'CheckPass',
            '-Username', self.username,
            '-Password', password
        ).output('json')

    def setPass(self, password:str):
        Users.run(
            'SetPass',
            '-Username', self.username,
            '-Password', password
        )

    def exists(self) -> bool:
        return Users.run(
            'Exists',
            '-Username', self.username
        ).output('json')

    def checkAuth(self, token:str):
        return (self.__token.read() == token)

    def resetAuth(self) -> str:
        from philh_myftp_biz.text import random

        token = random(10)
        self.__token.save(token)
        return token
    
# ================================================================================================================

# Declare 'Ffmpeg.exe' location
Ffmpeg = temp(
    name = 'ffmpeg',
    ext = 'exe',
    id = '0'
)
"""Ffmpeg.exe"""

# Check if 'Ffmpeg.exe' does not exist
if not Ffmpeg.exists():

    # Declare path for 'ffmpeg' zipfile
    zipfile = temp('ffmpeg', 'zip')
    """ffmpeg-release-essentials.zip"""

    # Download ffmpeg zipfile
    download(
        url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip',
        path = zipfile
    )

    # Open zipfile as an 'ZIP' object
    zip = ZIP(zipfile)

    # Search for 'ffmpeg.exe' in zipfile contents
    for f in zip.search('ffmpeg.exe'):

        # Extract 'ffmpeg.exe' to location declared earlier
        zip.extractFile(
            file = f,
            path = Ffmpeg
        )

        break

# ================================================================================================================

# Declare 'cookies.txt' location
Cookies = temp('cookies', 'txt', 'latest')
"""Cookies.txt"""

# Check if 'cookies.txt' does not exist
if not Cookies.exists():

    # Create Empty CookieJar
    CJ = MozillaCookieJar(str(Cookies))

    # Populate the CookieJar with cookies from FireFox
    for cookie in firefox():
        CJ.set_cookie(cookie)

    # Save the cookies to 'cookies.txt'
    CJ.save()

# ================================================================================================================

