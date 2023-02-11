"""Создание транзакции"""
import asyncio
import asyncpg
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

    async with connection.transaction(): # начать транзакцию
        await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'brand_2')")

    query = """SELECT brand_name FROM products.brand WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query) # выбрать марки и убедиться, что транзакция была зафиксирована
    print(brands)
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
