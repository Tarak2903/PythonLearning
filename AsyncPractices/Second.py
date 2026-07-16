import  asyncio

async def download_file():
    print("Downloading file...")
    await  asyncio.sleep(2)
    print("Downloaded the file")

async def process_file():
    print("Processing the file....")
    await  asyncio.sleep(2)
    print("Processed the file")

async def main():
    await asyncio.gather(
        download_file(),
        process_file()
    )

asyncio.run(main())