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
    os: Literal[*systems]
) -> list[str]:
    
    programs: list[str] = []
    
    for name, obj in vars(items).items():

        if hasattr(obj, os):

            programs += [name]

    return programs

@router.get('/get')
def _(
    name: str,
    os: Literal[*systems]
):

    program = getattr(items, name)

    data = getattr(program, os) ()

    name: str = data.name
    url:  URL = data.url

    tempfile = loc.temp.child(name)
    url.cache(tempfile)

    return FileResponse(
        path = tempfile.path,
        filename = name
    )
