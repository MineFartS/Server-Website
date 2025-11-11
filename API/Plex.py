from philh_myftp_biz.pc import Path, mkdir
from philh_myftp_biz.web import api
from fastapi import APIRouter
from typing import Literal

# Declare FastAPI router
router = APIRouter(
    prefix = '/Servers/Plex'
)

#
omdb = api.omdb()

#
movies = Path('E:/Plex/Media/Movies/')
shows = Path('E:/Plex/Media/Shows/')

@router.get('/download')
async def read_item(
    Title: str,
    Year: int,
    Type: Literal['movie', 'series']
) -> str:
    
    # Name of the movie file
    name = f'{Title} ({Year})'
    
    # If the media type is a show
    if Type == 'series':
        
        # Show Folder
        dir = shows.child(f'/{name}/')

        # If the folder already exists
        if dir.exists():
            
            # Return alert message
            return 'Show already exists'
        
        # If the folder does not exist
        else:
            
            # Create the folder
            mkdir(dir)
            
            # Return alert message
            return 'Show has been added to the download queue'

    # If the media type is a movie
    elif Type == 'movie':

        # Iter through all movie files
        for p in movies.children():
            
            # If the file has the same name as the movie
            if p.name() == name:
                
                # Return alert message
                return 'Movie already exists'
            
        # Path of Placeholder file
        todo = movies.child(f'/{name}.todo')

        # If the placeholder file exists
        if todo.exists():
            
            # Return alert message
            return 'Movie is already in the download queue'
        
        # If the placeholder file does not exist
        else:
            
            # Create the placeholder file
            todo.open('w')
            
            # Return alert message
            return 'Movie has been added to the download queue'


    return 'An unknown error has occurred'