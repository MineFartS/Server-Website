from philh_myftp_biz.terminal import ParsedArgs, Log
from philh_myftp_biz.process import Start
from __init__ import this, PIDstore
from os import getpid

#===========================================================

args = ParsedArgs()

#===========================================================
# PID Store

# Clear the PID store
PIDstore.save([])

# Store the pid of this execution
PIDstore += getpid()

max_pids = (args['workers'] + 1)

#===========================================================
# SSL Certificate

ssl_cert = this.file('certificates/cert')
ssl_key = this.file('certificates/key')

Log.VERB(f'SSL Certificate:\n{ssl_cert=}\n{ssl_key=}')

#===========================================================
# Uvicorn

p = Start(
    args = [
        'uvicorn', 'app:app',
        '--host', '0.0.0.0',
        '--ssl-certfile', ssl_cert,
        '--ssl-keyfile', ssl_key
    ],
    dir = this.child('/API/'),    
    terminal = 'pym'
)

#===========================================================
# Discover PIDs

Log.INFO('Discovering PIDs')

while len(PIDstore) <= max_pids:

    for line in p.stdcomb.split('\n'):

        if '[' in line:

            try:

                pid = int(line.split('[')[1].split(']')[0])

                if pid not in PIDstore:

                    Log.VERB(f'Discovered PID: {pid=}')

                    PIDstore += pid

            except ValueError:
                pass

Log.INFO(f'PIDs Discovered: {PIDstore.read()}')

#===========================================================

p.wait()