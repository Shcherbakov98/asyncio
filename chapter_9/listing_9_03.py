"""Получение конкретного товара"""
import asyncpg
import os
import sys
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from config import conf_load


routes = web.RouteTableDef()
DB_KEY = 'database'


@routes.get('/products/{id}')
async def get_product(request: Request) -> Response:
    try:
        # получить параметр product_id из URL
        str_id = request.match_info['id']
        product_id = int(str_id)
        query = "SELECT product_id, product_name, brand_id from products.product WHERE product_id = $1"

        pool: Pool = request.app[DB_KEY]

        # выполнить запрос для одного товара
        async with pool.acquire() as conn:
            result: Record = await conn.fetchrow(query, product_id)

        # если есть результат, то преобразовать его в json и отправить клиенту, иначе, 404
        if result is not None:
            return web.json_response(dict(result))
        else:
            raise web.HTTPBadRequest()
    except ValueError:
        raise web.HTTPBadRequest()


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


app = web.Application()
# добавить сопрограммы создания и уничтожения в обработчики инициализации и очистки
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)
