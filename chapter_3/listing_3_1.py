import socket


#  AF_INET - тип адреса, в данном случае ipv4 (хост и порт) SOCK_STREAM - протокол взаимодействия TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создает TCP сервер (серверный сокет)
#  установка socket.SO_REUSEADDR в 1,
#  позволит повторно использовать номер порта, после остановки и нового запуска приложения
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# задать адрес сокета (прослушивания) с портом
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen() # прослушивать запросы на подключение или "открыть почтовое отделение"

connection, client_address = server_socket.accept() # дождаться подключение и выделить клиенту сокет "почтовый ящик"
print(f'Получен запрос на подключение от {client_address}!')
