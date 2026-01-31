from philh_myftp_biz.modules import Module
from philh_myftp_biz.array import List
from philh_myftp_biz.file import JSON
from philh_myftp_biz.file import TXT
from philh_myftp_biz.pc import Path
from philh_myftp_biz.db import Ring
from typing import Generator

this = Module('E:/Website')
Users = Module('E:/Users')

root = this.dir.child('Root')

tokenRing = Ring('AuthTokens')

PIDstore = TXT(this.dir.child('/Indexer/__pycache__/PID.txt'))

# ================================================================================================================

class IndexRegistry:

    def __init__(self,
        dir: Path
    ):
        self.dir = dir
        self.__items: list[IndexedItem] = List(JSON(dir.child('index.json'), []))
        self.__search = List(JSON(Path('E:/Website/Root/_/Search/search.json'), []))

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
        
        # Check if file has a certain extension
        elif self.path.ext() in ['ini', 'config', 'ds_store', 'json', 'js', 'py', 'css']:
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
        from re import sub
        
        src = self.SRC()

        if src:

            mcode = sub(
                pattern = '<title>.*<\\/title>', 
                repl    = f'<title>{self.Title()}</title>', 
                string  = src.open().read()
            )
            
            self.path.open('w').write(mcode)

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
