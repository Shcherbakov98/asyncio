"""Сопрограммы на основе генераторов"""
import asyncio

@asyncio.coroutine
def coroutine():
    print('Засыпаю!')
    yield from asyncio.sleep(1)
    print('Проснулась!')

asyncio.run(coroutine())
