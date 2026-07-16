import asyncio

async def worker(name):
    try:
        while True:
            print(f"{name} Working...")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print(f"{name} Cleaning...")
        raise


async def main():
    tasks = []

    tasks.append(asyncio.create_task(worker("A")))
    tasks.append(asyncio.create_task(worker("B")))
    tasks.append(asyncio.create_task(worker("C")))

    await asyncio.sleep(4)

    print("\nCancelling all tasks...\n")

    for task in tasks:
        task.cancel()

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    print("\nGather returned:")
    print(results)


asyncio.run(main())