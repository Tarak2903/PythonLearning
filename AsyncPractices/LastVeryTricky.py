import asyncio

from AsyncPython.ExampleThread import start


async def work(name, t):
    print(f"{name} Start")
    await asyncio.sleep(t)
    print(f"{name} End")
    return name

async def main():
    t1 = asyncio.create_task(work("A", 3))
    t2 = asyncio.create_task(work("B", 2))

    await asyncio.sleep(1)

    print("X")

    result = await asyncio.gather(
        t1,
        t2,
        work("C", 1)
    )

    print(result)

asyncio.run(main())

