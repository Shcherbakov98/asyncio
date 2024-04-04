"""Иллюстрация условий"""
import asyncio
from asyncio import Condition


async def do_work(condition: Condition):
    while True:
        print('Ожидаю блокировки условия')
        # ждать возможности захватить условия; после захвата освободить блокировку
        async with condition:
            print('Блокировка захвачена, освобождаю ее и жду выполнения условия...')
            # ждать события; когда оно произойдет, заново захватить блокировку условия
            await condition.wait()
            print('Условие выполнено, вновь захватываю блокировку и начинаю работать...')
            await asyncio.sleep(1)
        # после выхода из контекста, освободить блокировку условия
        print('Работа закончена, блокировка освобождена')


async def fire_event(condition: Condition):
    while True:
        await asyncio.sleep(5)
        print('Перед уведомлением, захватываю блокировку условия...')
        async with condition:
            print('Блокировка захвачена, уведомляю всех исполнителей.')
            # уведомить все задачи о событии
            condition.notify_all()
        print('Исполнители уведомлены, освобождаю блокировку.')


async def main():
    condition = Condition()

    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))

asyncio.run(main())
