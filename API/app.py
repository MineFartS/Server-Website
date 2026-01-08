from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    middleware_class = CORSMiddleware,
    allow_origins = ['*']
)

from Routers.Apps.YouTube_Downloader import router
app.include_router(router)

from Routers.Apps.Bookmark import router
app.include_router(router)

from Routers.Login import router
app.include_router(router)

from Routers.Server.Plex import router
app.include_router(router)

from Routers.Server.Virtual_Machines import router
app.include_router(router)