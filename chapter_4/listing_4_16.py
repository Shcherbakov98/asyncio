"""Отмена медленного запроса"""
import asyncio
import aiohttp
from chapter_4 import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:

        url = 'https://ya.ru/'
        api_a = fetch_status(session, url)
        api_b = fetch_status(session, url, delay=3)

        # api_a = asyncio.create_task(fetch_status(session, url))
        # api_b= asyncio.create_task(fetch_status(session, url, delay=3))

        # done - содержит завершившиеся задачи или в результате исключения pending - ожидающие задачи
        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for task in pending:
            if task is api_b:
                print('API B слишком медленный отмена')
                task.cancel()
asyncio.run(main())
