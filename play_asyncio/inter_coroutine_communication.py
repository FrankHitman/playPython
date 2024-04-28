import asyncio

# 生产者协程
async def producer(queue, max_items):
    for i in range(max_items):
        print(f"Producing item {i}")
        await queue.put(i)
        await asyncio.sleep(1)

    # 发送结束信号
    await queue.put(None)

# 消费者协程
async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            print("Consumer received None, exiting")
            break
        print(f"Consuming item {item}")
        await asyncio.sleep(2)

async def main():
    queue = asyncio.Queue()

    # 启动生产者和消费者协程
    producer_task = asyncio.create_task(producer(queue, 5))
    consumer_task = asyncio.create_task(consumer(queue))

    # 等待协程结束
    await asyncio.gather(producer_task, consumer_task)

    print("All tasks finished")

if __name__ == "__main__":
    asyncio.run(main())

# output
# Franks-Mac:play_asyncio frank$ python inter_coroutine_communication.py
# Producing item 0
# Consuming item 0
# Producing item 1
# Consuming item 1
# Producing item 2
# Producing item 3
# Consuming item 2
# Producing item 4
# Consuming item 3
# Consuming item 4
# Consumer received None, exiting
# All tasks finished