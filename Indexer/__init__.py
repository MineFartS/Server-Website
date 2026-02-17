from philh_myftp_biz.modules import Module
from philh_myftp_biz.array import List
from philh_myftp_biz.file import JSON
from philh_myftp_biz.file import TXT
from philh_myftp_biz.pc import Path
from os import getpid

# ================================================================================================================
# INIT

this = Module('E:/Website')

root = this.child('Root')

# ================================================================================================================
# PID

PIDstore = TXT(this.child('/Indexer/__pycache__/PID.txt'))

PIDstore.save(getpid())

# ================================================================================================================
