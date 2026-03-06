from philh_myftp_biz.programs import COOKIES, FFMPEG
from fastapi.responses import FileResponse
from philh_myftp_biz.file import temp
from fastapi import APIRouter
from yt_dlp import YoutubeDL
from requests import get

# Declare FastAPI router
router = APIRouter(
    prefix = '/Apps/YouTube Downloader'
)

#
YTDLargs = lambda id, ext: {
    'ffmpeg_location': str(FFMPEG()), # 'Ffmpeg.exe' path
    'cookies': str(COOKIES()), # 'cookies.txt' path
    'output': str(temp('yt-download', ext, id))
}

@router.get('/video')
async def read_item( # pyright: ignore[reportRedeclaration]
    url: str
):

    #
    args = YTDLargs('mp4')

    #
    name = args['output'].split('/')[-1]

    # Set format to 'video'
    args['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

    # Set ext to 'mp4'
    args['merge_output_format'] = 'mp4'

    #
    YoutubeDL(args).download([url])

    #
    return name

@router.get('/audio')
async def read_item( # pyright: ignore[reportRedeclaration]
    url: str
):
    
    #
    args = YTDLargs('mp3')

    #
    name = args['output'].split('/')[-1]

    # Set format to 'audio'
    args['format'] = 'bestaudio/best'

    # Declare Post Processors
    args['postprocessors'] = [{
        'key': 'FFmpegExtractAudio', # Audio Only
        'preferredcodec': 'mp3', # mp3 codec
        'preferredquality': '192', # 192 kbps
    }]

    #
    YoutubeDL(args).download([url])

    #
    return name

@router.get('/thumbnail')
async def read_item( # pyright: ignore[reportRedeclaration]
    url: str
):

    #
    tempfile = temp('yt-download', 'jpg')

    #
    templURL = f"https://img.youtube.com/vi/{url.split('=')[1]}/" + "{}.jpg"

    #
    r = get(templURL.format('maxresdefault'))
    
    # If the maxresdefault does not exist
    if r.status_code != 200:
        r = get(templURL.format('hqdefault'))
    
    #
    with tempfile.open('wb') as f:
        f.write(r.content)

    # Return url and name
    return tempfile.seg()

@router.get('/file')
async def read_item(
    name: str
):
    # Return File
    return FileResponse(
        path = f'E:/__temp__/{name}',
        filename = name
    )
