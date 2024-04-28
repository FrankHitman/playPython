import asyncio

# 协程函数
async def coroutine(name):
    for i in range(3):
        print(f"Coroutine {name} is running")
        await asyncio.sleep(1)  # 自动切换到其他协程
        # 以下的代码也可以使用 await asyncio.sleep(0) 来主动让出 CPU 控制权

if __name__ == "__main__":
    # 创建并启动两个协程
    coro1 = coroutine("A")
    coro2 = coroutine("B")
    asyncio.run(asyncio.gather(coro1, coro2))

    print("All tasks finished")

# output
# Franks-Mac:play_asyncio frank$ python coroutine_auto_switch.py
# Traceback (most recent call last):
#   File "/Users/frank/play/playPython/play_asyncio/coroutine_auto_switch.py", line 14, in <module>
#     asyncio.run(asyncio.gather(coro1, coro2))
#   File "/Users/frank/.pyenv/versions/3.11.8/lib/python3.11/asyncio/runners.py", line 190, in run
#     return runner.run(main)
#            ^^^^^^^^^^^^^^^^
#   File "/Users/frank/.pyenv/versions/3.11.8/lib/python3.11/asyncio/runners.py", line 89, in run
#     raise ValueError("a coroutine was expected, got {!r}".format(coro))
# ValueError: a coroutine was expected, got <_GatheringFuture pending>
# sys:1: RuntimeWarning: coroutine 'coroutine' was never awaited
# Franks-Mac:play_asyncio frank$ python --version
# Python 3.11.8