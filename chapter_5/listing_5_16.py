"""Перемещение по курсору и выборка записей"""
import asyncpg
import asyncio
from config import conf_load
import os


async def main():
    await conf_load()
    conn = await asyncpg.connect(
        host=os.environ["host"],
        port=os.environ["port"],
        user=os.environ["user"],
        database=os.environ["database"],
        password=os.environ["password"],
    )

    async with conn.transaction():
        query = 'SELECT product_id, product_name FROM products.product'
        cursor = await conn.cursor(query) # создать курсор для запроса
        await cursor.forward(500) # сдвинуть курсор вперед на 500 записей
        products = await cursor.fetch(100) # получить следующие 100 записей
        for product in products:
            print(product)

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
