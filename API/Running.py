from philh_myftp_biz.pc import Task, cls
from __init__ import PIDstore

pid: int = PIDstore.read()

cls()

if pid:

    task = Task(pid)

    if task.exists():
        print('true')
    else:
        print('false')

else:

    print('false')