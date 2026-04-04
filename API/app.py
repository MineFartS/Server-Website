from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import FileResponse
from philh_myftp_biz.text import contains
from philh_myftp_biz.terminal import Log
from fastapi import FastAPI, Request
from importlib import import_module
from urllib.parse import parse_qs
from typing import Callable
from . import this

app = FastAPI()

#=====================================================================
# ROUTERS

for file in this.child('/API/Routers/').descendants:

    if (file.ext == 'py') and (file.name != '__init__'):

        imp: str = file.path
        imp = imp.split('/API/')[1]
        imp = imp.split('.')[0]
        imp = imp.replace('/', '.')
        imp = '.' + imp

        Log.VERB(f'Installing Router: {imp}')

        module = import_module(
            name = imp, 
            package = __package__
        )

        app.include_router(module.router)

#=====================================================================
# MIDDLEWARE

class CustomMiddleware(BaseHTTPMiddleware):

    async def _log(self,
        logger: Callable,
        request: Request, 
        status: str
    ) -> None:
        
        # GET: Parse URL params
        params = parse_qs(request.url.query)

        # POST: Read Form params
        if len(params) == 0:
            params = dict(await request.form())

        # Hide Sensitive info
        for name in params:
            if contains.any(name, ['password', 'token']):
                params[name] = '***'

        logger(f"""
 HOST  = {request.client.host}
 PATH  = {request.url.path}
PARAMS = {params}
METHOD = {request.method}
STATUS = {status}
""")
    
    async def dispatch(self, 
        request: Request, 
        call_next # pyright: ignore[reportMissingParameterType]
    ):

        await self._log(Log.VERB, request, '...')

        # Process the request
        response = await call_next(request)

        # Add the allow-all-origins header directly to the response
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"

        await self._log(Log.INFO, request, response.status_code)

        return response
    
    async def __call__(self, *args, **kwargs): # pyright: ignore[reportMissingParameterType]
        try:
            await super().__call__(*args, **kwargs)
        except Exception as e:
            Log.FAIL(str(e))

Log.VERB('Installing Middleware')

app.add_middleware(CustomMiddleware)

#=====================================================================
# FAVICON

Log.VERB('Installing Favicon')

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    
    path = this.child('/Root/_/main.ico')
    
    return FileResponse(path.path)

#=====================================================================

Log.INFO('Uvicorn Service Started')
