from fastapi.responses import FileResponse
from philh_myftp_biz.pc import Path, loc
from philh_myftp_biz.web import URL
from fastapi import APIRouter
from typing import Literal
from . import items

systems = 'Windows', 'MacOS', 'Linux'

router = APIRouter(
    prefix = '/Media/Programs'
)

@router.get('/list')
def _(
    os: Literal[*systems] # pyright: ignore[reportInvalidTypeForm]
) -> list[str]:
    
    programs: list[str] = []
    
    for name, obj in vars(items):

        if hasattr(obj, os):

            programs += [name]

    return programs

@router.get('/get')
def _(
    name: str,
    os: Literal[*systems] # pyright: ignore[reportInvalidTypeForm]
):

    program = getattr(items, name)

    os_data = getattr(program, os) ()

    name: str = os_data.name
    url: URL = os_data.url

    tempfile = loc.temp.child(name)

    url.cache(tempfile)

    return FileResponse(tempfile.path)
