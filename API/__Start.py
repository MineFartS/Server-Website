from starlette.middleware.cors import CORSMiddleware
from philh_myftp_biz.web import FirewallException
from philh_myftp_biz.process import Start
from philh_myftp_biz.terminal import Log
from importlib import import_module
from philh_myftp_biz import VERBOSE
from . import this, PIDstore
from fastapi import FastAPI
from os import getpid

if __name__ == '__main__':#================================================================================================

    #===========================================================
    # Firewall

    fe = FirewallException('Uvicorn')
    fe.set(8000)

    #===========================================================
    # Uvicorn

    p = Start(

        args = [
            'uvicorn', 'API.__Start:app',
            '--host', '0.0.0.0',
            '--ssl-certfile', this.file('certificates/cert'),
            '--ssl-keyfile', this.file('certificates/key'),
            *([] if VERBOSE else ['--workers', 2])
        ],

        dir = this,
        
        terminal = 'pym'

    )

    PIDstore.save(list(p._task.PIDs))

    p.wait()

    #===========================================================

elif __name__ == 'API.__Start':#================================================================================================

    #===========================================================

    PIDstore += getpid()

    #===========================================================

    app = FastAPI()

    app.add_middleware(
        middleware_class = CORSMiddleware,
        allow_origins = ['*']
    )

    #===========================================================

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