"""Задание таймаута для as_completed (действует для группы задач, задачи не снимаются при исключении по таймауту)"""
import asyncio
import aiohttp
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://ya.ru/', 1),
                    fetch_status(session, 'https://ya.ru/', 10),
                    fetch_status(session, 'https://ya.ru/', 10)]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print('result->', result)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')

        for task in asyncio.tasks.all_tasks():
            print('task->', task)

asyncio.run(main())
