"""Простой асинхронный генератор"""
import asyncio
from util import delay, async_timed


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer


@async_timed()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Получено число {number}')


if __name__ == '__main__':
    asyncio.run(main())
