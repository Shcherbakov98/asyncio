"""Выполнение HTTP-запроса с помощью транспортного механизма и протокола"""
import asyncio
from asyncio import Transport, Future, AbstractEventLoop
from typing import Optional


class HTTPGetClientProtocol(asyncio.Protocol):
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host: str = host
        self._future: Future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b''

    #  ждать внутренний будущий объект, пока не будет получен ответ от сервера
    async def get_response(self):
        return await self._future

    def _get_request_bytes(self) -> bytes:
        request = f"GET / HTTP/1.1\r\n" \
                  f"Connection: close\r\n" \
                  f"Host: {self._host}\r\n\r\n"

        return request.encode()

    def connection_made(self, transport: Transport):
        print(f'Создано подключение к {self._host}')
        self._transport = transport
        # после того как подключение установлено, использовать транспорт для отправки запроса
        self._transport.write(self._get_request_bytes())

    def data_received(self, data: bytes):
        print(f'Получены данные!')
        # получив данные, сохранить их во внутреннем буфере
        self._response_buffer += data

    def eof_received(self) -> Optional[bool]:
        # после закрытия подключения завершить будущий объект, скопировав в него данные из буфера
        self._future.set_result(self._response_buffer.decode())
        return False

    # если подключение было закрыто без ошибок, не делать ничего; иначе, завершить будущий объект исключением
    def connection_lost(self, exc: Optional[Exception]) -> None:
        if exc is None:
            print('Подключение без ошибок.')
        else:
            self._future.set_exception(exc)


