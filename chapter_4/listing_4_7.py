"""Завершение допускающих ожидание объектов не по порядку (порядок возврата детерменнирован, а порядок выполнения - нет"""
import asyncio
from util import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)

asyncio.run(main())
