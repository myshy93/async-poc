import asyncio
from asyncio import sleep


# convert to tasks
# run sequential
# gather
# delay

async def greet():
    print("Hello Endava!")


async def count_persons():
    print("COUNTER: Counting....")
    await sleep(2)
    print("COUNTER: Count done.")
    return 290


async def start_projector():
    print("PROJECTOR: Projector is starting....")
    await sleep(1)
    print("PROJECTOR: Projector started.")


async def deploy_screen():
    print("SCREEN: Deploying the screen....")
    for i in range(5):
        print(f"SCREEN: Deployed {25 * i}%")
        await sleep(1)
    print("SCREEN: Screen deployed")


async def main():
    t1 = asyncio.create_task(deploy_screen())
    t2 = asyncio.create_task(start_projector())
    t3 = asyncio.create_task(count_persons())

    await asyncio.gather(t1, t2, t3)

    print(t3.result())


if __name__ == "__main__":
    asyncio.run(main())
