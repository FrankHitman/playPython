import signal
import sys
import threading
import time


class PlayThread(threading.Thread):
    def __init__(self):
        super(PlayThread, self).__init__()
        self.stop_event = threading.Event()
    def run(self):
        last_sync_time = time.time()
        print('init time {}'.format(last_sync_time))

        while not self.stop_event.is_set():
            time.sleep(5)
            now = time.time()

            if now - last_sync_time > 20:
                last_sync_time = now
                print('update time {}'.format(last_sync_time))
            else:
                print('not update at {}'.format(now))

    def join(self, timeout=None):
        self.stop_event.set()
        super(PlayThread, self).join(timeout)


if __name__ == '__main__':
    a = PlayThread()
    a.setDaemon(True)
    a.start()

    def signal_handler(signal_num, stack_frame):
        print('stop')
        a.join(10)
        sys.exit()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    while 1:
        time.sleep(1)

# output
# init time 1631952912.5249288
# not update at 1631952917.5252917
# not update at 1631952922.5259979
# not update at 1631952927.5266664
# update time 1631952932.5273564
# not update at 1631952937.5278816
# not update at 1631952942.528287
# stop
# not update at 1631952947.528752
