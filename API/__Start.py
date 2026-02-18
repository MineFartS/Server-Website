from philh_myftp_biz.terminal import ParsedArgs, Log
from philh_myftp_biz.process import Start
from philh_myftp_biz.array import List
from philh_myftp_biz.file import JSON
from os import getpid

#===========================================================

args = ParsedArgs()
args.Arg(
    name = 'workers',
    default = 2
)

#===========================================================
# Install API Package

try:
    import Website_API

except:
    from subprocess import run
    from sys import executable
    
    run(
        args = [executable, '-m', 'pip', 'install', '.'],
        cwd = 'E:/Website/API/Package/'
    )

finally:
    from Website_API import this

#===========================================================
# PID Store

PIDstore: List[int] = List(JSON(this.child('/API/__pycache__/PID.json')))

# Clear the PID store
PIDstore.save([])

# Store the pid of this execution
PIDstore += getpid()

max_pids = (args['workers'] + 1)

#===========================================================
# SSL Certificate

ssl_cert = this.file('certificates/cert')
ssl_key = this.file('certificates/key')

Log.VERB(f'SSL Certificate: {ssl_cert=} | {ssl_key=}')

#===========================================================
# Uvicorn

p = Start(

    args = [
        'uvicorn', 'app:app',
        '--host', '0.0.0.0',
        '--ssl-certfile', ssl_cert,
        '--ssl-keyfile', ssl_key,
        '--workers', args['workers']
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