import time
import os
from celery import Celery

app = Celery("task", broker="pyamqp://guest@localhost//")

# extract the time consuming portion of code and place it into
# a separate block

def clear_dir():
    mydir='Backend/media/folanja/certificate'
    filelist = [ f for f in os.listdir(mydir)  ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))

@app.task
def sleep_asynchronously():
    """
    This function simulates a task that takes 20 seconds to
    execute to completion.
    """
    while(True):
        clear_dir()
        time_length=10#3600*24#each day
        time.sleep(time_length)


print("Let's begin!")

# this is how the sleep_asynchronously() method is invoked to
# execute asynchronously

# sleep_asynchronously.delay()
sleep_asynchronously()

'''how to run it:
just use " celery -A task worker --loglevel=info" in terminal "
'''
