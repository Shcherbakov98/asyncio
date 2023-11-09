"""Оконечная точка brands в приложении Starlette"""
import asyncpg
import sys
import os
from asyncpg import Record
from asyncpg.pool import Pool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from starlette.routing import Route
from typing import List, Dict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from config import conf_load


async def create_database_pool():
    print('Создается пул подключений.')
    await conf_load()
    pool: Pool = await asyncpg.create_pool(
            host=os.environ["host"],
            port=os.environ["port"],
            user=os.environ["user"],
            password=os.environ["password"],
            database=os.environ["database"],
            min_size=6,
            max_size=6,
    )
    app.state.DB = pool


async def destroy_database_pool():
    print('Уничтожается пул подключений.')
    pool: Pool = app.state.DB
    await pool.close()


async def brands(request: Request) -> Response:
    db: Pool = request.app.state.DB
    async with db.acquire() as conn:
        results: List[Record] = await conn.fetch('SELECT brand_id, brand_name FROM products.brand')
        result_as_dict: List[Dict] = [dict(brand) for brand in results]
        return JSONResponse(result_as_dict)


app = Starlette(
    routes=[Route('/brands', brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database_pool]
)
