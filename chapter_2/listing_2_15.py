from asyncio import Future
import asyncio


def make_result() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future=future))  # создать задачу, которая асинхронно установит значение future
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)  # ждать 1 с, прежде чем установить значение
    future.set_result(42)


async def main():
    future = make_result()
    print(f'Будущий объект готов? {future.done()}')
    value = await future  # приостановить main, пока значение future не установлено
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())
