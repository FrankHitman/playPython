# encoding=utf-8
import time
import threading

def child():
    time.sleep(5)
    print('child thread sleep 5 sec')

if __name__ == '__main__':
    print(time.time())
    print('main thread daemonic is ', threading.current_thread().isDaemon())
    # ch = threading.Thread(target=child, daemon=False)
    ch = threading.Thread(target=child, daemon=True)
    print('child thread daemonic is ', ch.daemon)
    ch.start()
    # ch.join()  # this will sleep 8 sec
    time.sleep(3)
    print('main thread sleep 3 sec ', time.time())
    # ch.join()  # this will sleep 5 sec


# ch = threading.Thread(target=child, daemon=False)
# ----output-----
# 1555748562.02735
# main thread daemonic is  False
# child thread daemonic is  False
# main thread sleep 3 sec  1555748565.031872
# child thread sleep 5 sec

# ch = threading.Thread(target=child, daemon=True)
# ----output-----
# 1555748643.7766056
# main thread daemonic is  False
# child thread daemonic is  True
# main thread sleep 3 sec  1555748646.7808406

# 守护线程：主线程退出，但子线程会被强行退出(尤其是子线程还在活动时)，守护线程一般是一个等待客户请求的服务器，如果没有客户提出退出，就不会退出
# 在线程start之前，设置daemon属性thread.setDaemon(True)，就表示主线程要退出时，不用等待子线程结束，然后强制结束子线程。
# 默认Daemon属性是false，也可以显示调用thread.setDaemon(False)
# if set child thread daemon=false, then main thread will waite the child thread finished
# if set child thread daemon=true, then main thread will not waite the child thread finished
# if set child thread daemon=true, but use thread.join() in main thread, then main thread will waite the child thread finished

