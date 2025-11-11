from typing import Generator
from philh_myftp_biz.modules import Module
from philh_myftp_biz.pc import Path
from philh_myftp_biz.db import Ring
from fastapi import UploadFile

from philh_myftp_biz.file import temp, ZIP
from http.cookiejar import MozillaCookieJar
from philh_myftp_biz.web import download
from browser_cookie3 import firefox

this = Module('E:/Website')
Users = Module('E:/Users')

root = this.dir.child('Root')

tokenRing = Ring('AuthTokens')

# ================================================================================================================

class IndexRegistry:

    def __init__(self,
        dir: Path
    ):
        from philh_myftp_biz.array import new
        from philh_myftp_biz.file import json

        self.dir = dir
        self.__items: list[IndexedItem] = new(json(dir.child('index.json'), []))
        self.__search = new(json(Path('E:/Website/Root/_/Search/search.json'), []))

    def items(self) -> Generator['IndexedItem']:
        for p in self.dir.children():
            yield IndexedItem(p)

    def build(self):

        # Clear all items from registry
        self.__items.save([])

        # Scan all items in directory
        for i in self.items():

            # Get JSON data for item
            data = i.toJSON()

            # Append data to current registry
            self.__items += data

            # Append data to search registry
            self.__search += data

        # Sort items in registry
        self.__items.sort(lambda x: x['Title'])

class IndexedItem:

    def __init__(self,
        path: Path
    ):
        self.path = path

        if self.path.isdir():
            self.dir = self.path
        else:
            self.dir = self.path.parent()

    def URL(self) -> str:

        # Get base url from file path
        url = str(self.path).replace('E:/Website/Root', '', 1)

        # Check if file is '.href'
        if self.path.ext() == 'href':
            # Return text contents of file
            return str(self.path.open().read()).strip()
        
        # Check if filename is 'index.html'
        elif url.split('/')[-1] == 'index.html':
            # Return url of parent directory
            return '/'.join(url.split('/')[:-1]) + '/'

        else:
            # Returm base url
            return url

    def Visible(self) -> bool:

        # Check if is directory
        if self.path.isdir():
            # Return True unless 'hide.ini' exists inside the directory
            return (not self.path.child('Hide.ini').exists())

        # Check if filename starts with '__'
        elif self.path.seg().startswith('__'):
            return False
        
        # Check if file has ext: ('ini', 'config', 'ds_store', 'json', 'js')
        elif self.path.ext() in ['ini', 'config', 'ds_store', 'json', 'js', 'css']:
            return False
        
        # Check if filename is 'index.html'
        elif self.path.seg() == 'index.html':
            return False
        
        else:
            return True

    def Title(self) -> str:

        # Check if is dir
        if self.path.isdir():
            # Return Name of Dir
            return self.path.name()

        # Check if filename is 'index.html'
        elif self.path.seg() == 'index.html':

            # Check if file is in website root directory
            if self.dir == root:
                return "Phil's Server"

            else:
                # Return Name of parent directory
                return self.path.parent().name()

        else:
            # Return Name of file
            return self.path.name()

    def SRC(self) -> Path | None:

        if self.path.isdir():
            return None
        
        elif self.path.seg() == 'index.html':

            template = self.path.parent().sibling('__template__.html')
        
            if self.dir.child('Protect.ini').exists():
                src = self.path

            elif template.exists():
                src = template

            else:
                src = root.child('index.html')

            try:
                src.open().read()
                return src
            except (UnicodeDecodeError, FileNotFoundError):
                pass

    def Update(self):
        
        src = self.SRC()

        if src:

            code: str = src.open().read()
            
            code = \
                code[:code.find('<title>')] + \
                f'<title>{self.Title()}</title>' + \
                code[code.find('</title>')+8:]
            
            self.path.open('w').write(code)

    def filter(self, term:str=None):
        if term:
            return (term.lower() in self.path.seg().lower())
        else:
            return True

    def toJSON(self):
        return {
            'URL': self.URL(),
            'Visible': self.Visible(),
            'Title': self.Title(),
            'SRC': str(self.SRC()),
            'Path': str(self.path)
        }

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
    id = 'latest'
)
"""Ffmpeg.exe"""

# Check if 'Ffmpeg.exe' does not exist
if False:#not Ffmpeg.exists():

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

        # Exit Generator
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

