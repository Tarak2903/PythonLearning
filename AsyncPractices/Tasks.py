import asyncio
from threading import Thread
import time
async def cook_food():
    print("Started soaking")
    await asyncio.sleep(2)
    print("Cooking completed")

async def watch_tv():
    print("Watching add before")
    await asyncio.sleep(2)
    print("add was completed")


async def main():
    task1=asyncio.create_task(cook_food())
    await watch_tv()
    await task1

asyncio.run(main())

