"""Ручное управление транзакцией"""
import asyncio
import asyncpg
from config import conf_load
from asyncpg.transaction import Transaction
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
    transaction: Transaction = connection.transaction() # создаем экземпляр транзакции
    await transaction.start() # начать транзакцию
    try:
        await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'brand_5')")
        await connection.execute("INSERT INTO products.brand VALUES(DEFAULT, 'brand_6')")
    except asyncpg.PostgresError:
        print('Ошибка, транзакция откатывается!')
        await transaction.rollback() # если было исключение откатить
    else:
        print('Ошибки нет, транзакция фиксируется!')
        await transaction.commit() # если исключения не было, зафиксировать

    query = """SELECT brand_name FROM products.brand WHERE brand_name LIKE 'brand_%'"""
    brands = await connection.fetch(query)
    print(f'Результат запроса: {brands}')

    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
