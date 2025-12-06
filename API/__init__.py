from philh_myftp_biz.modules import Module
from philh_myftp_biz.file import PKL
from philh_myftp_biz.pc import Task

# ==================================================

this = Module('E:/Website')

PIDstore = PKL(this.dir.child('/API/__pycache__/PID.pkl'))

# ==================================================

task: Task = None

if PIDstore.read():

    task = Task(PIDstore.read())

# ==================================================