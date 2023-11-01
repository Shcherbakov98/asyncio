"""Подключение к базе данных о товарах"""
import asyncpg
import os
import sys
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
from typing import List, Dict
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from config import conf_load


routes = web.RouteTableDef()
DB_KEY = 'database'


# создать пул подключений к БД и сохранить его в экземпляре приложения
async def create_database_pool(app: Application):
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

    app[DB_KEY] = pool


# уничтожить пул в экземпляре приложения
async def destroy_database_pool(app: Application):
    print('Уничтожается пул подключений.')
    pool: Pool = app[DB_KEY]
    await pool.close()


# запросить все марки и вернуть результат клиенту
@routes.get('/brands')
async def brands(request: Request) -> Response:
    connection: Pool = request.app[DB_KEY]
    brand_query = 'SELECT brand_id, brand_name from products.brand'
    results: List[Record] = await connection.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return web.json_response(result_as_dict)


app = web.Application()
# добавить сопрограммы создания и уничтожения в обработчики инициализации и очистки
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)

