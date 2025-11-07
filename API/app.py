from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi import FastAPI

# -------------------------------------------------------------------------------------

app = FastAPI()
app.add_middleware(
    middleware_class = CORSMiddleware,
    allow_origins = ['*']
)

# -------------------------------------------------------------------------------------

from YouTube_Downloader import router
app.include_router(router)

from Bookmark import router
app.include_router(router)

from Login import router
app.include_router(router)

# -------------------------------------------------------------------------------------

@app.get("/temp")
async def read_item(
    f: str,
    d: bool = False
):
    """
    Get a file from the Temporary Directory

    f: File Name
    d: Download
    """
    from philh_myftp_biz.pc import Path
    
    # Get path of the file
    path = Path('E:/__temp__').child(f)

    # Check if 'd' (download) is enabled
    if d:
        filename = path.seg()
    else: 
        filename = None

    # Check if the file exists
    if path.exists():
        # Return File
        return FileResponse(
            path = str(path),
            filename = filename
        )

# -------------------------------------------------------------------------------------