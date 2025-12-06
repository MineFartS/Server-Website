from starlette.middleware.cors import CORSMiddleware
from __init__ import PIDstore, this
from fastapi import FastAPI
from uvicorn import run
from os import getpid

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

# Store the pid of this execution
PIDstore.save(getpid())

# Start the api via uvicorn
run(
    app = app,
    host = '0.0.0.0',
    ssl_certfile = this.file('certificates/cert').path,
    ssl_keyfile = this.file('certificates/key').path
)
