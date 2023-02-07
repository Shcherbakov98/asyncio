"""Подключение к базе данных Postgres от имени пользователя по умолчанию"""
import asyncpg
import asyncio
import os
from config import conf_load


async def main():
    await conf_load()
    conn = await asyncpg.connect(
        host=os.environ["host"],
        user=os.environ["user"],
        database=os.environ["database"],
        password=os.environ["password"],
    )
    version = conn.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await conn.close()

asyncio.run(main())
