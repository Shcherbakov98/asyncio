"""Тестирование сопрограммы retry"""
import asyncio
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from chapter_10.listing_10_09 import retry, TooManyRetries


async def main():
    async def always_fail():
        raise Exception('Упал')

    async def always_timeout():
        await asyncio.sleep(1)

    try:
        await retry(always_fail, max_retries=3, timeout=.1, retry_interval=.1)
    except TooManyRetries:
        print('Слишком много попыток!')

    try:
        await retry(always_timeout, max_retries=3, timeout=.1, retry_interval=.1)
    except TooManyRetries:
        print('Слишком много попыток!')

if __name__ == '__main__':
    asyncio.run(main())
