import asyncio
from asyncio import CancelledError
from util import delay


async def main():
    log_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not log_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            log_task.cancel()

    try:
        await log_task
    except CancelledError:
        print('Наша задача была снята')

asyncio.run(main())
