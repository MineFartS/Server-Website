from typing import Literal, TYPE_CHECKING
from philh_myftp_biz.file import temp
from __init__ import Ffmpeg, Cookies
from fastapi import APIRouter
from yt_dlp import YoutubeDL

if TYPE_CHECKING:
    from philh_myftp_biz.pc import Path

# Declare FastAPI router
router = APIRouter(
    prefix = '/Apps/YouTube Downloader'
)

ydl_args = {
    'ffmpeg_location': str(Ffmpeg), # 'Ffmpeg.exe' path
    'cookies': str(Cookies) # 'cookies.txt' path
}
"""Base Arguements for YoutubeDL"""

def Video(url:str) -> 'Path':
        
    #
    args = ydl_args.copy()

    #
    path = temp(
        name = 'yt-download',
        ext = 'mp4'
    )

    # Set format to 'video'
    args['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

    # Set ext to 'mp4'
    args['merge_output_format'] = 'mp4'

    # Set output path
    args['outtmpl'] = str(path)

    #
    YoutubeDL(args).download([url])

    return path


def Audio(url:str) -> 'Path':
        
    #
    args = ydl_args.copy()

    #
    path = temp(
        name = 'yt-download',
        ext = 'mp3'
    )

    # Set format to 'audio'
    args['format'] = 'bestaudio/best'

    # Declare Post Processors
    args['postprocessors'] = [{
        'key': 'FFmpegExtractAudio', # Audio Only
        'preferredcodec': 'mp3', # mp3 codec
        'preferredquality': '192', # 192 kbps
    }]

    # Set output path
    args['outtmpl'] = str(path)

    #
    YoutubeDL(args).download([url])

    return path


def Thumbnail(url:str) -> 'Path':
        
    #
    args = ydl_args.copy()

    #
    path = temp(
        name = 'yt-download',
        ext = 'png'
    )

    # TODO

    # Set output path
    args['outtmpl'] = str(path)

    #
    YoutubeDL(args).download([url])

    return path


@router.get('/get')
async def read_item(
    url: str,
    format: Literal['video', 'audio', 'thumbnail']
) -> dict[Literal['url', 'name'], str]:
    """
    Download a YouTube Video
    """

    # Check if selected format is 'video'
    if format == 'video':
        path = Video(url)
    
    # Check if selected format is 'audio'
    elif format == 'audio':
        path = Audio(url)

    # Check if selected format is 'thumbnail'
    elif format == 'thumbnail':
        path = Thumbnail(url)

    # Return url and name
    return {
        'url': f'/temp?d=true&f={path.seg()}', # Video Path (for API)
        'name': f'YouTube Download.{path.ext()}' # Name to Download with 
    }