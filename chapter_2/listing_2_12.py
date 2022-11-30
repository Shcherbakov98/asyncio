import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))

    try:
        res = await asyncio.wait_for(delay_task, timeout=1)
        print(res)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')

asyncio.run(main())
