"""Обработка запросов по мере завершения (FIRST_COMPLETED)"""
import asyncio
import aiohttp
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:

        url = 'https://ya.ru/'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url))]

        # done - содержит завершившиеся задачи или в результате исключения pending - ожидающие задачи
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

    for done_task in done:
        print(await done_task)

asyncio.run(main())
