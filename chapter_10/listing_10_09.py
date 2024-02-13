"""Сопрограмма retry"""
import asyncio
import logging
from typing import Callable, Awaitable


class TooManyRetries(Exception):
    pass


async def retry(
        coro: Callable[[], Awaitable],
        max_retries: int,
        timeout: float,
        retry_interval: float):
    for retry_num in range(0, max_retries):
        try:
            #  ждать ответа, пока не истечет заданный таймаут
            return await asyncio.wait_for(coro(), timeout=timeout)
        except Exception as e:
            #  если получено исключение, протоколировать его
            #  и ждать в течении заданного интервала перед повторной попыткой
            logging.exception(
                f'Во время ожидания произошло исключение (попытка {retry_num}), попробую еще раз.', exc_info=e
            )
            await asyncio.sleep(retry_interval)
        #  если было слишком много неудачных попыток, возбудить исключение, уведомляющее об этом
    raise TooManyRetries()
