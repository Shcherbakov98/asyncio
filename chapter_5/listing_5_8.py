"""Синхронное и конкурентное выполнение запросов"""
import asyncio
import asyncpg
from config import conf_load
import os
from util import async_timed


product_query = \
    """
SELECT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
FROM products.product as p
JOIN products.sku as s on s.product_id = p.product_id
JOIN products.product_color as pc on pc.product_color_id = s.product_color_id
JOIN products.product_size as ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = 2249
    """

async def query_product(pool):
    async with pool.acquire() as conn:
        return await conn.fetchrow(product_query)


@async_timed()
async def query_products_sync(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    await conf_load()
    async with asyncpg.create_pool(
        host=os.environ["host"],
        port=os.environ["port"],
        user=os.environ["user"],
        password=os.environ["password"],
        database=os.environ["database"],
        min_size=6,
        max_size=6,
    ) as pool: # создать пул с 6 подключениями
        await query_products_sync(pool, 10000)
        await query_products_concurrently(pool, 10000)

if __name__ == "__main__":
    asyncio.run(main())
