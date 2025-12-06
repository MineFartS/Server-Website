from fastapi.responses import FileResponse
from fastapi import APIRouter

# Declare FastAPI router
router = APIRouter()

@router.get("/temp")
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