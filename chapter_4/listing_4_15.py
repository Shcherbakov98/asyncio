"""Использование таймаутов в wait"""
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
                    asyncio.create_task(fetch_status(session, url, delay=3))]

        # done - содержит завершившиеся задачи или в результате исключения pending - ожидающие задачи
        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            res = await done_task
            print(res)

asyncio.run(main())
