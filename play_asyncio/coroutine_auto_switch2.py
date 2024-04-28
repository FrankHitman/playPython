import asyncio

# 协程函数
async def coroutine(name):
    for i in range(3):
        print(f"Coroutine {name} is running")
        await asyncio.sleep(1)  # 自动切换到其他协程

async def main():
    # 创建两个协程并同时运行
    coro1 = coroutine("A")
    coro2 = coroutine("B")
    await asyncio.gather(coro1, coro2)

if __name__ == "__main__":
    asyncio.run(main())

    print("All tasks finished")

# output
# Franks-Mac:play_asyncio frank$ python coroutine_auto_switch2.py
# Coroutine A is running
# Coroutine B is running
# Coroutine A is running
# Coroutine B is running
# Coroutine A is running
# Coroutine B is running
# All tasks finished