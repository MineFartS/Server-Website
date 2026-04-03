from philh_myftp_biz.web import FirewallException
from philh_myftp_biz import VERBOSE
from . import this, PIDstore
from uvicorn import run
from os import getpid

FirewallException('Uvicorn').set(8000)

PIDstore.save([getpid()])

run(
    app = 'API.app:app',
    host = '0.0.0.0',
    port = 8000,
    workers = (None if VERBOSE else 2),
    ssl_certfile = this.file('certificates/cert').path,
    ssl_keyfile = this.file('certificates/key').path,
    log_level = "error"
)
