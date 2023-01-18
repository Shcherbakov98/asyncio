import asyncio
from asyncio import AbstractEventLoop
import socket
import logging
import signal
from typing import List


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    """
    Отвечает за обработку данных, связанных с одним подключением (в дальнейшем обертывается в задачу)
    connection - сокет клиента
    loop - цикл событий
    """
    # пока данные приходят с сокета, отправлять их обратно
    # в бесконечном цикле ожидаем данных от клиента
    # если сообщение 'boom' инициируем исключение
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('got data!')
            if data == b'boom\r\n':
                raise Exception("Неожиданная ошибка сети")
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        # в случае ошибки логируем ее
        logging.exception(ex)
    finally:
        # в любом случае закрываем соединение по окончанию задачи
        connection.close()

# список echo задач (для дальнейшего их закрытия)
echo_tasks = []

async def connection_listener(server_socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получено сообщение от {address}')
        # после подключения клиента, создаем задачу, ожидающую данные от клиента
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)

class GracefulExit(SystemExit):
    """Кастомное исключение в результате которого вызывается функция закрытия задач"""
    pass

def shutdown():
    """
    Функция вызывающаяся при сигналах SIGTERM и SIGINT
    Инициирует вызов кастомного исключения, который, вызывает функцию закрытия всех задач
    """

    raise GracefulExit()

async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    # функция дает каждой задаче 2 секунды таймаута на выполнение перед принудительным снятием
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            # Здесь мы ожидаем истечение таймаута
            pass

async def main():
    # создаем серверный сокет; AF_INET - ipv4; SOCK_STREAM - TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # привязываем адрес к объекту серверного сокета (какой ip и порт прослушивать)
    server_address = ('127.0.0.1', 8000)
    server_socket.bind(server_address)

    # сокет неблокирующий (все блокирующие методы сразу возвращают управление)
    server_socket.setblocking(False)
    # прослушиваем запросы на подключение
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown())
    await connection_listener(server_socket, loop)

# создаем цикл событий
loop = asyncio.new_event_loop()
try:
    # выполняем главную сопрограмму пока все задачи не выполнятся
    loop.run_until_complete(main())
except GracefulExit:
    # если возникает наше исключение, даем время на завершение задач
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    # в любом случае закрываем цикл событий
    loop.close()
