from starlette.middleware.cors import CORSMiddleware
from philh_myftp_biz.modules import Module
from fastapi import FastAPI
from uvicorn import run

this = Module('E:/Website')

app = FastAPI()
app.add_middleware(
    middleware_class = CORSMiddleware,
    allow_origins = ['*']
)

from Routers.YouTube_Downloader import router
app.include_router(router)

from Routers.Bookmark import router
app.include_router(router)

from Routers.Login import router
app.include_router(router)

from Routers.Plex import router
app.include_router(router)

from Routers.other import router
app.include_router(router)

run(
    app = app,
    host = '0.0.0.0',
    ssl_certfile = this.file('certificates/cert').path,
    ssl_keyfile = this.file('certificates/key').path
)
