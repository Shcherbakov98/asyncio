"""
Создание эхо-сервера с помощью серверных объектов
"""
import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ServerState:
    def __init__(self):
        self._writers = []

    # добавить клиента в состояние сервера и создать задачу эхо-копирования
    async def add_client(self, reader: StreamReader, writer: StreamWriter):
        self._writers.append(writer)
        await self._on_connect(writer)
        asyncio.create_task(self._echo(reader, writer))

    # после подключения нового клиента сообщить ему, сколько клиентов подключено
    # и уведомить остальных о новом клиенте
    async def _on_connect(self, writer):
        writer.write(f'Добро пожаловать! Число подключенных пользователей {len(self._writers)}!\n'.encode())
        await writer.drain()
        await self._notify_all('Подключился новый пользователь!\n')

    # обработать эхо-копирование ввода при отключении клиента
    # и уведомить остальных пользователей об отключении
    async def _echo(self, reader: StreamReader, writer: StreamWriter):
        try:
            while (data := await reader.readline()) != b'':
                writer.write(data)
                await writer.drain()
            self._writers.remove(writer)
            await self._notify_all(f'Клиент отключился. Осталось пользователей: {len(self._writers)}!\n')
        except Exception as e:
            logging.exception('Ошибка чтения данных от клиента.', exc_info=e)
            self._writers.remove(writer)

    # вспомогательный метод отправки сообщения всем остальным пользователям
    # если отправить сообщение не удалось, удалить данного пользователя
    async def _notify_all(self, message: str):
        for writer in self._writers:
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as e:
                logging.exception('Ошибка записи данных клиенту.', exc_info=e)
                self._writers.remove(writer)


async def main():
    server_state = ServerState()

    # при получении нового клиента добавить его в состояние сервера
    async def client_connected(reader: StreamReader, writer: StreamWriter) -> None:
        await server_state.add_client(reader, writer)

    # запустить сервер и обслуживать запросы бесконечно
    server = await asyncio.start_server(client_connected, '127.0.0.1', '8000')

    async with server:
        await server.serve_forever()

asyncio.run(main())
