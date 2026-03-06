from starlette.middleware.cors import CORSMiddleware
from philh_myftp_biz.terminal import Log
from importlib import import_module
from fastapi import FastAPI
from __init__ import this

app = FastAPI()

app.add_middleware(
    middleware_class = CORSMiddleware,
    allow_origins = ['*']
)

for file in this.child('/API/Routers/').descendants:

    if (file.ext == 'py') and (file.name != '__init__'):

        imp: str = file.path
        imp = imp.split('/API/')[1]
        imp = imp.split('.')[0]
        imp = imp.replace('/', '.')

        Log.INFO(f'Installing Router: {imp}')

        app.include_router(
            router = import_module(imp).router
        )
