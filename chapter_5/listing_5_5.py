"""Вставка случайных марок"""
import asyncio
import asyncpg
from typing import List, Tuple, Union
from config import conf_load
from random import sample
import os


def load_common_words() -> List[str]:
    with open('common_words.txt') as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str,]]]:
    return [(words[index].strip(),) for index in sample(range(1000), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands_q = "INSERT INTO products.brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands_q, brands)


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
    await insert_brands(common_words=common_words, connection=connection)


if __name__ == '__main__':
    asyncio.run(main())
