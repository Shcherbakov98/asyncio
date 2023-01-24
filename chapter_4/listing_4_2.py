"""Отправка веб-запроса с помощью aiohttp"""
import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://ya.ru/'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} равно {status}')

if __name__ == "__main__":
    asyncio.run(main())
