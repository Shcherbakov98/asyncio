"""Использование сопрограммы execute для выполнение команд create и insert"""
import asyncio
from chapter_5.listing_5_2 import CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, CREATE_PRODUCT_COLOR_TABLE, \
CREATE_PRODUCT_SIZE_TABLE, CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT
import asyncpg
from config import conf_load
import os


async def main():
    # загружаем конфиг (в виртуальное окружение загружаются параметры подключения к бд)
    await conf_load()
    # создаем подключение к бд
    connection = await asyncpg.connect(
        host=os.environ["host"],
        port=os.environ["port"],
        user=os.environ["user"],
        database=os.environ["database"],
        password=os.environ["password"]
    )

    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT
    ]
    print('Создается база данных warehouse...')
    for statement in statements:
        status = await connection.execute(statement)
        print('status->', status)
    print('База данных warehouse создана')
    await connection.close()

if __name__ == "__main__":
    asyncio.run(main())