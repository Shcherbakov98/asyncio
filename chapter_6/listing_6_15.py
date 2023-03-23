"""Цикл событий в каждом процессе"""
import asyncio
import asyncpg
from config import conf_load
from util import async_timed
import os
from typing import List, Dict
from concurrent.futures.process import ProcessPoolExecutor


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
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)

def run_in_new_loop(num_queries: int) -> List[Dict]:
    async def run_queries():
        await conf_load()
        async with asyncpg.create_pool(
            host=os.environ["host"],
            port=os.environ["port"],
            user=os.environ["user"],
            password=os.environ["password"],
            database=os.environ["database"],
            min_size=6,
            max_size=6,
        ) as pool:
            return await query_products_concurrently(pool, num_queries)
    # выполнять запросы в новом цикле событий и преобразовывать их в словари
    results = [dict(result) for result  in asyncio.run(run_queries())]
    return results

@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    pool = ProcessPoolExecutor()
    # создать пять процессов, каждый со своим циклом событий, для выполнения запросов
    tasks = [loop.run_in_executor(pool, run_in_new_loop, 10000) for _ in range(5)]
    all_result = await asyncio.gather(*tasks) # ждем получение всех результатов
    total_queries = sum([len(result) for result in all_result])
    print(f'Извлечено товаров из базы данных: {total_queries}.')

if __name__ == "__main__":
    asyncio.run(main())
