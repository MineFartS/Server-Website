from philh_myftp_biz.process import Start
from philh_myftp_biz.file import JSON
from philh_myftp_biz.array import List
from os import getpid

try:
    import Website_API

except ModuleNotFoundError:
    from subprocess import run
    from sys import executable
    
    run(
        args = [executable, '-m', 'pip', 'install', '.'],
        cwd = 'E:/Website/API/Package/'
    )

finally:
    from Website_API import this

#===========================================================

PIDstore: List[int] = List(JSON(this.dir.child('/API/__pycache__/PID.json')))

# Clear the PID store
PIDstore.save([])

# Store the pid of this execution
PIDstore += getpid()

#===========================================================

#
p = Start(
    args = [
        'uvicorn', 'app:app',
        '--host', '0.0.0.0',
        '--ssl-certfile', this.file('certificates/cert'),
        '--ssl-keyfile', this.file('certificates/key')
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

#===========================================================