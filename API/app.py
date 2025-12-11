from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

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
