"""Класс нагрузочного тестирования"""
import asyncio
from concurrent.futures import Future
from asyncio import AbstractEventLoop
from typing import Callable, Optional
from aiohttp import ClientSession


class StressTest:
    def __init__(
            self,
            loop: AbstractEventLoop,
            url: str,
            total_request: int,
            callback: Callable[[int, int], None],
    ):
        self._completed_requests: int = 0
        self._load_test_future: Optional[Future] = None
        self._loop = loop
        self._url = url
        self._total_requests = total_request
        self._callback = callback
        self._refresh_rate = total_request // 100

    # Начать отправку запросов и сохранить будущий объект,
    # чтобы в последствии можно было отменить тест
    def start(self):
        # run_coroutine_threadsafe - принимает сопрограмму и
        # потокобезопасным образом подает функцию для выполнения и возвращает future
        future = asyncio.run_coroutine_threadsafe(self._make_requests(), self._loop)
        self._load_test_future = future

    # чтобы отменить тест, нужно вызвать метод cancel объекта _load_test_future
    def cancel(self):
        if self._load_test_future:
            # run_coroutine_threadsafe - принимает функцию (не сопрограмму) и потокобезопасным образом
            # планирует выполнение функции на следующей итерации цикла событий
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str):
        try:
            await session.get(url)
        except Exception as e:
            print(e)
        self._completed_requests += 1
        # после того как отправка 1 % запросов завершена, вызвать функцию обратного вызова
        # и передать ей число завершенных запросов и общее число запросов
        if self._completed_requests % self._refresh_rate == 0 or self._completed_requests == self._total_requests:
            self._callback(self._completed_requests, self._total_requests)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [self._get_url(session, self._url) for _ in range(self._total_requests)]
        await asyncio.gather(*reqs)
