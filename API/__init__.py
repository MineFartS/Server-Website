from philh_myftp_biz.modules import Module
from philh_myftp_biz.file import PKL

this = Module('E:/Website')

PIDstore = PKL(this.dir.child('/API/__pycache__/PID.pkl'))
