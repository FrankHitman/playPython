import gevent
from gevent.event import AsyncResult
result = AsyncResult()
gevent.spawn(lambda : 1/0).link(result)
try:
    result.get()
except ZeroDivisionError:
    print('ZeroDivisionError')

# -----output----
# ZeroDivisionError
# Traceback (most recent call last):
#   File "src/gevent/greenlet.py", line 766, in gevent._greenlet.Greenlet.run
#   File "/home/sdy/play_python/palyPython/play_gevent/coroutine_communicate_with_exception.py", line 4, in <lambda>
#     gevent.spawn(lambda : 1/0).link(result)
# ZeroDivisionError: integer division or modulo by zero
# 2019-04-13T08:15:23Z <Greenlet at 0x7f8ec7bfccb0: <lambda>> failed with ZeroDivisionError
