"""Вставка случайных товарок и SKU"""
import asyncio
import asyncpg
from typing import List, Tuple
from config import conf_load
from random import sample, randint
from  chapter_5.listing_5_5 import load_common_words
import os


def gen_products(
        common_words: List[str],
        brand_id_start: int,
        brand_id_end: int,
        products_to_create: int,
)-> List[Tuple[str, int]]:
    products = []
    for _ in range(products_to_create):
        desc = [common_words[index].strip() for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append(("".join(desc), brand_id))

    return products


def gen_skus(product_id_start: int, product_id_end: int, sku_to_create: int) -> List[Tuple[int, int, int]]:
    skus = []
    for _ in range(sku_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 2)
        color_id = randint(1, 2)

        skus.append((product_id, size_id, color_id))

    return skus


async def main():
    common_words = load_common_words()

    await conf_load()
    connection = await asyncpg.connect(
        host=os.environ["host"],
        port=os.environ["port"],
        user=os.environ["user"],
        database=os.environ["database"],
        password=os.environ["password"],
    )
    product_tuples = gen_products(common_words, brand_id_start=112, brand_id_end=211, products_to_create=1000)
    await connection.executemany("INSERT INTO products.product VALUES(DEFAULT, $1, $2)", product_tuples)

    sku_tuples = gen_skus(product_id_start=2001, product_id_end=3000, sku_to_create=100000)
    await connection.executemany("INSERT INTO products.sku VALUES(DEFAULT, $1, $2, $3)", sku_tuples)

    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
