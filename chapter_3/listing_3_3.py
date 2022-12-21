import socket


# создаем серверный сокет; AF_INET - ipv4; SOCK_STREAM - TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# привязываем адрес к объекту серверного сокета (какой ip и порт прослушивать)
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
# прослушиваем запросы на подключение
server_socket.listen()

connections = []

try:
    while True:
        # принимаем подключение клиента (клиентского сокета)
        # connection-объект подключения (клиентский сокет для чтения данных от клиента и записи адресованных ему данных)
        # client_address - адрес клиента
        # блокируется приложение на ожидании подключения
        connection, client_address = server_socket.accept()
        # добавляем сокет клиента в общий список сокетов клиентов
        connections.append(connection)

        # проходим по всем подключениям (клиентским сокетам) из общего списка
        for con in connections:
            # временный буфер (для каждого клиента свой)
            buffer = b''
            # пока последние символы в буфере не равны '\r\n' (окончанию строки)
            while buffer[-2:] != b'\r\n':
                # получаем данные от клиента
                # блокируется приложение на ожидании получения сообщения от клиента
                data = con.recv(2)
                # если нет данных останавливаем цикл и переходим к следующему клиенту
                if not data:
                    break
                else:
                    # если есть данные в клиентском сокете печатаем данные и добавляем в буфер
                    print(f'Получены данные: {data}!')
                    buffer += data
            # печатаем общие данные полученные для конкретного клиента
            print(f'Получены все данные: {buffer}')

            connection.send(buffer)
finally:
    # закрываем серверный сокет в любом случае при завершении программы даже с ошибкой
    server_socket.close()