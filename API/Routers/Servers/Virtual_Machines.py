from philh_myftp_biz.modules import Module
from fastapi import APIRouter
from fastapi.responses import FileResponse
from philh_myftp_biz.file import temp

# Declare FastAPI router
router = APIRouter(
    prefix = '/Servers/Virtual Machines'
)

# Virtual Machine Module
VM = Module('E:/Virtual Machines')

# 
templ = """
full address:s:philh.myftp.biz
pcb:s:{id}
server port:i:2179
negotiate security layer:i:0
"""

@router.get('/connectRDP')
async def read_item(
    name: str
):

    id = VM.cap('ID', f'User-{name}')

    code = templ.format(id=id)

    file = temp(
        name = 'connect',
        ext = 'rdp'
    )

    with file.open('w') as f:
        f.write(code)

    return FileResponse(
        path = str(file),
        filename = f'{name}.rdp',
        media_type = 'application/octet-stream'
    )
