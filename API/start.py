#from __init__ import this
from philh_myftp_biz import run
from philh_myftp_biz.pc import script_dir

script_dir(__file__).cd()

API = run(
    args = [
        'uvicorn',
        'app:app',
        '--host', '0.0.0.0',
        '--workers', 1
    ],
    terminal = 'pym',
    autostart = False
)

#    ssl_certfile = this.file('certificates', 'cert').path,
#    ssl_keyfile = this.file('certificates', 'key').path

if __name__ == '__main__':

    API.start()

    """
    for wf in this.watch():
        API.restart()
    """ 