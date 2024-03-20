"""Операции с событиями"""
import asyncio
import functools
from asyncio import Event


def trigger_event(event: Event):
    print('Активируется событие!')
    event.set()


async def do_work_on_event(event: Event):
    print('Ожидаю события...')
    await event.wait()  # ждать события
    # когда событие произойдет, блокировка снимается и мы продолжаем работу
    print('Работаю')
    await asyncio.sleep(1)
    print('Работа закончена!')
    event.clear()  # сбросить событие, в результате чего последующие обращения к wait блокируются


async def main():
    event = Event()
    asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event))
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))

asyncio.run(main())
