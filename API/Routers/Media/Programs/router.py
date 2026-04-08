from fastapi.responses import FileResponse
from philh_myftp_biz.pc import Path
from fastapi import APIRouter
from . import list as _list
from typing import Literal

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

    tfile: Path = getattr(program, os) ()

    return FileResponse(tfile.path)

