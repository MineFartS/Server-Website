from fastapi.responses import HTMLResponse, FileResponse
from philh_myftp_biz.web import URL
from fastapi import APIRouter
from ... import Users

apiURL = URL('https://philh.myftp.biz:8000/Server/Users/')

# Declare FastAPI router
router = APIRouter(
    prefix = '/Server/Users'
)

@router.get("/open")
async def _(
    username: str, 
    path: str
):
    
    url = apiURL.child('open')

    url.params = {
        'username': username,
        'path': path
    }

    if url.params['path'][-1] != '/':
        url.params['path'] += '/'
    
    _path = Users.child(f'/philh/{username}/Website{path}')

    if _path.is_dir:

        _html = f"<html> <body> <h1>{username}/Website/{path}</h1>"

        for child in _path.children:

            _url = url.copy()
            _url.params[path] += child.name

            _html += f'<a href="{_url}">{child.name}</a> <br>'

        _html += "</body></html>"

        return HTMLResponse(_html)

    else:
        return FileResponse(_path.path)
