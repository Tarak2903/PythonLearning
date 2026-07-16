import asyncio

async def say_hello(name):
    print("Starting...")
    await asyncio.sleep(2)
    print(f"Hello {name}")
    return "Done"

async def main():
    result = await say_hello("Tarak")
    print(result)

asyncio.run(main())