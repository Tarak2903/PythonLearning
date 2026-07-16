import asyncio

from selenium.webdriver.common.devtools.v148.tracing import end

from AsyncPython.ExampleThread import start


async def worker(name, delay):
    print(f"{name} Start")
    await asyncio.sleep(delay)
    print(f"{name} End")
    return name

async def main():
    t1 = asyncio.create_task(worker("A", 2))
    t2 = asyncio.create_task(worker("B", 1))

    result = await asyncio.gather(t1, worker("C", 3))

    print(result)

    print(await t2)

asyncio.run(main())

