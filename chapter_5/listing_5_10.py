"""Обработка ошибки транзакции"""
import asyncio
import asyncpg
from config import conf_load
import logging
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

    try:
        async with connection.transaction(): # начать транзакцию
            insert_brand = "INSERT INTO products.brand VALUES(999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)  # команда insert завершится неудачно, из-за дубликата ключа (pk)
    except Exception:
        logging.exception('Ошибка при выполнении транзакции') # протоколируем ошибку
    finally:
        query = """SELECT brand_name FROM products.brand WHERE brand_name LIKE 'big_%'"""
        brands = await connection.fetch(query) # выбрать марки и убедиться, что ничего не вставлено
        print(f'Результат запроса: {brands}')
        await connection.close()

        await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
