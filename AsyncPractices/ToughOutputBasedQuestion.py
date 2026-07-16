import asyncio

async def worker(name, t):
    print(f"{name} Start")
    await asyncio.sleep(t)
    print(f"{name} End")
    return name

async def main():
    t1 = asyncio.create_task(worker("A", 3))
    t2 = asyncio.create_task(worker("B", 1))
    t3 = asyncio.create_task(worker("C", 2))

    print(await t2)

    print(await t3)

    print(await t1)

asyncio.run(main())



