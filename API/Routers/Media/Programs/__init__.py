from fastapi.responses import FileResponse
from philh_myftp_biz.file import temp
from philh_myftp_biz.pc import Path
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

    name = program.__name__
    ext: str = data.ext
    url:  URL = data.url

    tempfile = temp(name, ext, 0)
    url.cache(tempfile)

    return FileResponse(
        path = tempfile.path,
        filename = f'{name}.{ext}'
    )
