from __init__ import task

if task:

    if task.exists():
        print('true')
    else:
        print('false')

else:

    print('false')