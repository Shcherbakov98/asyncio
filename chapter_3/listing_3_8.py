import asyncio
import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    """
    Отвечает за обработку данных, связанных с одним подключением (в дальнейшем обертывается в задачу)
    connection - сокет клиента
    loop - цикл событий
    """
    # пока данные приходят с сокета, отправлять их обратно
    # в бесконечном цикле ожидаем данных от клиента
    while data := await loop.sock_recv(connection, 1024):
        await loop.sock_sendall(connection, data)

async def listen_for_connections(server_socket: socket, loop: AbstractEventLoop):
    """
    Отвечает за прием подключений к серверному сокету клиентов
    """
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {address}')
        # после подключения клиента, создаем задачу, ожидающую данные от клиента
        asyncio.create_task(echo(connection, loop))

async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # запускаем сопрограмму, для прослушивания порта на предмет подключений
    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())