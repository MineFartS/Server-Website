from __init__ import this
from philh_myftp_biz import run, Args
from philh_myftp_biz.pc import script_dir

script_dir(__file__).cd()

args = Args()

if len(args) == 1:
    workers = args[0]
else:
    workers = 1

API = run(
    args = [
        'uvicorn',
        'app:app',
        '--host', '0.0.0.0',
        '--workers', workers,
        '--ssl-certfile', this.file('certificates', 'cert').path,
        '--ssl-keyfile', this.file('certificates', 'key').path
    ],
    terminal = 'pym',
    autostart = False
)

if __name__ == '__main__':

    API.start()

    """
    for wf in this.watch():
        API.restart()
    """ 