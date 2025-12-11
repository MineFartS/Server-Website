from __init__ import PIDstore, this
from philh_myftp_biz import run
from os import getpid

# Clear the PID store
PIDstore.save([])

# Store the pid of this execution
PIDstore += getpid()

#
p = run(
    args = [
        'uvicorn', 'app:app',
        '--host', '0.0.0.0',
        '--ssl-certfile', this.file('certificates/cert'),
        '--ssl-keyfile', this.file('certificates/key'),
        '--workers', 2
    ],
    dir = this.dir.child('/API/'),
    terminal = 'pym'
)

while True:

    for line in p.stdcomb.split('\n'):

        if '[' in line:

            try:

                pid = int(line.split('[')[1].split(']')[0])

                if pid not in PIDstore:

                    print(f'{pid=}')

                    PIDstore += pid

            except ValueError:
                pass
