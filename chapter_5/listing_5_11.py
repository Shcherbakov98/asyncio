"""Вложенная транзакция"""
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

    async with connection.transaction():
        await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'my_new_brand1')")
        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO products.product_color VALUES(1, 'Blue')")
        except Exception as ex:
            logging.exception('Ошибка при вставке цвета товара игнорируется', exc_info=ex)

        await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'my_new_brand2')")


    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
