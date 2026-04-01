from philh_myftp_biz.terminal import ParsedArgs, Log
from starlette.middleware.cors import CORSMiddleware
from philh_myftp_biz.web import FirewallException
from importlib import import_module
from philh_myftp_biz.pc import Path
from . import this, PIDstore
from fastapi import FastAPI
from uvicorn import run
from sys import prefix
from os import getpid

#===========================================================

fe = FirewallException('Uvicorn')

fe.set(Path(prefix + '\\Scripts\\uvicorn.exe'))

#===========================================================

args = ParsedArgs()

#===========================================================
# PID Store

# Clear the PID store
PIDstore.save([])

# Store the pid of this execution
PIDstore += getpid()

#===========================================================
# APP

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
        imp = '.' + imp

        Log.INFO(f'Installing Router: {imp}')

        module = import_module(
            name = imp, 
            package = __package__
        )

        app.include_router(module.router)

#===========================================================
# RUN

run(
    app = app,
    host = '0.0.0.0',
    ssl_certfile = this.file('certificates/cert').path,
    ssl_keyfile = this.file('certificates/key').path
)
