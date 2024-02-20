"""Состояние гонки в однопоточной программе"""
import asyncio

counter: int = 0


async def increment():
    global counter
    tmp_counter = counter
    tmp_counter += 1
    await asyncio.sleep(0.01)
    counter = tmp_counter


async def main():
    global counter
    for _ in range(1000):
        tasks = [asyncio.create_task(increment()) for _ in range(100)]
        await asyncio.gather(*tasks)
        print(f'Счетчик равен {counter}')
        assert counter == 100
        counter = 0

asyncio.run(main())
