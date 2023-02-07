"""Подключение к базе данных Postgres от имени пользователя по умолчанию"""
import asyncpg
import asyncio


async def main():
    conn = await asyncpg.connect(
        host='127.0.0.1',
        user='postgres',
        database='postgres',
        password='123',
    )
    version = conn.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await conn.close()

asyncio.run(main())
