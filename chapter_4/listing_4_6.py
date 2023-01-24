"""Конкурентное выполнение запросов с помощью gather"""
import asyncio
from aiohttp import ClientSession
from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://ya.ru/' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)

asyncio.run(main())
