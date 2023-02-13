"""Получение заданного числа элементов с помощью асинхронного генератора"""
import asyncpg
import asyncio
from config import conf_load
import os


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


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
        product_generator = conn.cursor(query) # создать курсор для запроса
        async for product in take(product_generator, 5):
            print(product)
        print('Получены первые пять товаров')

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
