"""Изучение поведения wait по умолчанию"""
import asyncio
import aiohttp
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://ya.ru/')),
                    asyncio.create_task(fetch_status(session, 'https://ya.ru/'))]

        # done - содержит завершившиеся задачи или в результате исключения pending - ожидающие задачи
        # default asyncio.wait(return_when=ALL_COMPLETED)
        done, pending = await asyncio.wait(fetchers)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

    for done_task in done:
        result = await done_task
        print(result)

asyncio.run(main())
