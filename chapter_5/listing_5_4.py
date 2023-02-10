"""Вставка и выборка марок"""
import asyncio
import asyncpg
from asyncpg import Record
from typing import List
from config import conf_load
import os


async def main():
    await conf_load()
    connection = await asyncpg.connect(
        host=os.environ["host"],
        port=os.environ["port"],
        user=os.environ["user"],
        database=os.environ["database"],
        password=os.environ["password"],
    )
    await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'Seven')")

    brand_query = 'SELECT brand_id, brand_name FROM products.brand'
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()

if __name__ == '__main__':
    asyncio.run(main())
