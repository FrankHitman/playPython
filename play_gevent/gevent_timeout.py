# encoding=utf-8
import gevent
from gevent import Timeout

timeout = Timeout(2)  # 2 seconds
timeout.start()

def wait():
    gevent.sleep(10)

# try:
#     gevent.spawn(wait).join()
# except Timeout:
#     print('Could not complete')

class TooLong(Exception):
    print "too long"

with Timeout(2,TooLong):
    gevent.sleep(10)

    # gevent.spawn(wait).join()


