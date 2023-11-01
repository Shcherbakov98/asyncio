"""Оконечная точка для создания товара"""
import asyncpg
import os
import sys
from aiohttp import web
from http import HTTPStatus
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg.pool import Pool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from config import conf_load

routes = web.RouteTableDef()
DB_KEY = 'database'


@routes.post('/product')
async def create_product(request: Request) -> Response:
    PRODUCT_NAME = 'product_name'
    BRAND_ID = 'brand_id'

    if not request.can_read_body:
        raise web.HTTPBadRequest()

    body = await request.json()

    if PRODUCT_NAME in body and BRAND_ID in body:
        db: Pool = request.app[DB_KEY]

        async with db.acquire() as conn:
            try:
                await conn.execute(
                    '''INSERT INTO products.product(product_id, product_name, brand_id) VALUES(DEFAULT, $1, $2)''',
                    body[PRODUCT_NAME],
                    body[BRAND_ID]
                )
            except asyncpg.ForeignKeyViolationError:
                raise web.HTTPBadRequest()
            return web.Response(status=HTTPStatus.CREATED)
    else:
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
