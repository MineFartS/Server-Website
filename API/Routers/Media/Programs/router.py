from fastapi.responses import FileResponse
from fastapi import APIRouter
from . import list as _list
from typing import Literal

from philh_myftp_biz.pc import Path, loc
from philh_myftp_biz.web import URL

systems = 'Windows', 'MacOS', 'Linux'

router = APIRouter(
    prefix = '/Media/Programs'
)

router.get('list')
def _(
    os: Literal[*systems] # pyright: ignore[reportInvalidTypeForm]
) -> list[str]:
    
    programs: list[str] = []
    
    for name, obj in vars(_list):

        if hasattr(obj, os):

            programs += [name]

    return programs

router.get('get')
def _(
    name: str,
    os: Literal[*systems] # pyright: ignore[reportInvalidTypeForm]
) -> FileResponse | None:

    program = getattr(_list, name)

    os_data = getattr(program, os) ()

    name: str = os_data.name
    url: URL = os_data.url

    tempfile = loc.temp.child(name)

    url.cache(tempfile)

    return FileResponse(tempfile.path)
