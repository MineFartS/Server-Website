from philh_myftp_biz.modules import Module
from . import root

Users = Module('E:/Users/')

for user in Users.cap('List'):

    src = Users.child(f'/philh/{user['Username']}/')
    
    dst = root.child(f'/Server/Users/Share/{user['Username']}/')

    dst.set_access.full()

    src.link(dst)
    