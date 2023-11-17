"""Создание и уничтожение пула подключений к базе данных"""
import asyncpg
from aiohttp.web_app import Application
from asyncpg.pool import Pool

DK_KEY = 'database'


async def create_database_pool(
        app: Application,
        host: str,
        port: int,
        user: str,
        database: str,
        password: str,
):
    pool: Pool = await asyncpg.create_pool(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        min_size=6,
        max_size=6
    )

    app[DK_KEY] = pool


async def destroy_database_pool(app: Application):
    pool: Pool = app[DK_KEY]
    await pool.close()
