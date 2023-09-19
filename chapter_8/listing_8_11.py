"""Асинхронный командный SQL-клиент"""
import asyncio
import asyncpg
import os
import sys
import tty
from collections import deque
from asyncpg.pool import Pool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from chapter_8.listing_8_05 import create_stdin_reader
from chapter_8.listing_8_07 import *
from chapter_8.listing_8_08 import read_line
from chapter_8.listing_8_09 import MessageStore
from config import conf_load


async def run_query(query: str, pool: Pool, message_store: MessageStore):
    async with pool.acquire() as conn:
        try:
            result = await conn.fechrow(query)
            await message_store.append(f'Выбрано {len(result)} строк по запросу: {query}')
        except Exception as e:
            await message_store.append(f'Получено исключение {e} от: {query}')


async def main():
    tty.setcbreak(0)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(callback=redraw_output, max_size=rows - 1)

    stdin_reader = await create_stdin_reader()

    await conf_load()
    async with asyncpg.create_pool(
        host=os.environ["host"],
        port=os.environ["port"],
        user=os.environ["user"],
        database=os.environ["database"],
        password=os.environ["password"],
        min_size=6,
        max_size=6
    ) as pool:
        while True:
            query = await read_line(stdin_reader)
            asyncio.create_task(run_query(query, pool, messages))
