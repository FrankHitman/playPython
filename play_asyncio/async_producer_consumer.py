# encoding=utf-8
import asyncio


async def consumer(queue):
    while True:
        try:
            message = queue.get_nowait()
            print("Consumer %s" % message)
            await asyncio.sleep(1)
        except asyncio.queues.QueueEmpty:
            break
        # queue.task_done()


async def producer(n, queue):
    x = 0
    while x < n:
        x += 1
        queue.put_nowait(x)
        print('Produce %s' % x)
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()
    task1 = asyncio.create_task(producer(4, queue))
    task2 = asyncio.create_task(consumer(queue))

    # await queue.join()
    await task1
    await task2
    # task1.cancel()
    # task2.cancel()


asyncio.run(main())


# this example is simple to play_greenlet and play_generate's xxx_producer_consumer.py
# ----output------
# Produce 1
# Consumer 1
# Produce 2
# Consumer 2
# Produce 3
# Consumer 3
# Produce 4
# Consumer 4
