import gevent

def beep(interval):
    # while True:
    print("Beep %s" % interval)
    gevent.sleep(interval)

for i in range(2):
    gevent.spawn(beep, i)

beep(20)