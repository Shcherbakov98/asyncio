import socket


# создаем серверный сокет; AF_INET - ipv4; SOCK_STREAM - TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# привязываем адрес к объекту серверного сокета (какой ip и порт прослушивать)
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
# прослушиваем запросы на подключение
server_socket.listen()
# сокет неблокирующий (все блокирующие методы сразу возвращают управление
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass # игнорируем исключение говорящее: у меня сейчас нет данных в сокете, попробуй вызвать меня позже

        for con in connections:
            try:
                buffer = b''
                while buffer[-2:] != b'\r\n':
                    data = con.recv(2)
                    if not data:
                        break
                    else:
                        print(f'Получены данные: {data}!')
                        buffer += data
                print(f'Все данные: {buffer}')
                connection.send(buffer)
            except BlockingIOError:
                pass
finally:
    server_socket.close()