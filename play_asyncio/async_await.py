import asyncio
import time

async def say_after(delay, what):
    # in this case asyncio.sleep(delay)==time.sleep(delay)
    await asyncio.sleep(delay)
    print(f" at {time.strftime('%X')}")
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
