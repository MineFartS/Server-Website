from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from __init__ import this
from uvicorn import run

app = FastAPI()
app.add_middleware(
    middleware_class = CORSMiddleware,
    allow_origins = ['*']
)

from YouTube_Downloader import router
app.include_router(router)

from Bookmark import router
app.include_router(router)

from Login import router
app.include_router(router)

from Plex import router
app.include_router(router)

from other import router
app.include_router(router)

run(
    app = app,
    host = '0.0.0.0',
    ssl_certfile = this.file('certificates/cert').path,
    ssl_keyfile = this.file('certificates/key').path
)
