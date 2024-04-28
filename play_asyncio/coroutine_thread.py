import threading
import time
import asyncio

# 协程函数
async def coroutine(name):
    for i in range(3):
        print(f"Coroutine {name} is running")
        await asyncio.sleep(1)

# 线程函数
def thread_function(name):
    for i in range(3):
        print(f"Thread {name} is running")
        time.sleep(1)

if __name__ == "__main__":
    # 创建并启动两个协程
    coro1 = coroutine("A")
    coro2 = coroutine("B")
    asyncio.run(coro1)
    asyncio.run(coro2)

    # 创建并启动两个线程
    thread1 = threading.Thread(target=thread_function, args=("X",))
    thread2 = threading.Thread(target=thread_function, args=("Y",))
    thread1.start()
    thread2.start()

    # 等待线程结束
    thread1.join()
    thread2.join()

    print("All tasks finished")

# output
# Franks-Mac:play_asyncio frank$ python coroutine_thread.py
# Coroutine A is running
# Coroutine A is running
# Coroutine A is running
# Coroutine B is running
# Coroutine B is running
# Coroutine B is running
# Thread X is running
# Thread Y is running
# Thread X is running
# Thread Y is running
# Thread X is running
# Thread Y is running
# All tasks finished