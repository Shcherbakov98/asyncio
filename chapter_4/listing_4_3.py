"""Задание таймаутов в aiohttp клиентской части"""
import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
    ten_mils = aiohttp.ClientTimeout(total=.01)
    async with session.get(url=url, timeout=ten_mils) as result:
        return result.status

async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://ya.ru/')

asyncio.run(main())
