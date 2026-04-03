from starlette.middleware.base import BaseHTTPMiddleware
from philh_myftp_biz.terminal import Log
from fastapi import FastAPI, Request
from importlib import import_module
from urllib.parse import parse_qs
from . import this

app = FastAPI()

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

class CustomMiddleware(BaseHTTPMiddleware):

    def _log(self,
        request: Request, 
        status: str
    ) -> None:
        Log.INFO(f"""
 HOST  = {request.client.host}
 PATH  = {request.url.path}
PARAMS = {parse_qs(request.url.query)}
METHOD = {request.method}
STATUS = {status}
""")
    
    async def dispatch(self, 
        request: Request, 
        call_next # pyright: ignore[reportMissingParameterType]
    ):

        self._log(request, '...')

        # Process the request
        response = await call_next(request)

        # Add the allow-all-origins header directly to the response
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"

        self._log(request, response.status_code)

        return response

Log.VERB('Installing Middleware')
app.add_middleware(CustomMiddleware)

Log.INFO('Uvicorn Service Started')
