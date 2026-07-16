import asyncio

async def download():
    for i in range(5):
        print("Downloading")
        await  asyncio.sleep(1)

async def main():
    task=asyncio.create_task(download())
    for i in range(5):
        print("Doing other work...")
        await asyncio.sleep(1)

asyncio.run(main())