import asyncio
from util import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} c')
    await asyncio.sleep(delay=delay_seconds)
    print(f'сон в течении {delay_seconds} c закончен')
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())
