"""Потоковая обработка результатов"""
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

    query = 'SELECT product_id, product_name FROM products.product'

    async with conn.transaction():
        async for product in conn.cursor(query):
            print(product)

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
