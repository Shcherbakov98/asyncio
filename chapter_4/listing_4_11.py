"""Обработка исключений при использовании wait"""
import asyncio
import aiohttp
from util import async_timed
from chapter_4 import fetch_status
import logging

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_req = fetch_status(session, 'https://ya.ru/')
        bad_req = fetch_status(session, 'python://ya.ru/')

        fetchers = [asyncio.create_task(good_req),
                    asyncio.create_task(bad_req)]

        # done - содержит завершившиеся задачи или в результате исключения pending - ожидающие задачи
        # default asyncio.wait(return_when=ALL_COMPLETED)
        done, pending = await asyncio.wait(fetchers)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

    for done_task in done:
        # result = await done_task возбудит исключение
        if done_task.exception() is None:
            print(done_task.result())
        else:
            logging.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())

asyncio.run(main())
