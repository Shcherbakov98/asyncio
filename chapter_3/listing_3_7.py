import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

# автоматически выбирает реализацию системы уведомлений для конкретной ОС
selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.setblocking(False)
server_socket.listen()

# регистрируем серверный сокет, который будет прослушивать подключения от клиентов
selector.register(server_socket, selectors.EVENT_READ)

while True:
    # создать селектор с таймаутом 1
    # блокирует выполнение, пока не произойдет какое-либо событие (действия с сокетами)
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=5)

    # если нет событий, сообщить об этом
    if len(events) == 0:
        print('Событий нет, еще подожду!')

    for event, _ in events:
        # получаем сокет для которого произошло событие в списке событий
        event_socket = event.fileobj

        # если событие произошло с серверным сокетом, значит произошла попытка подключения клиента
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {address}')
            # регистрируем сокет подключившегося пользователя
            selector.register(connection, selectors.EVENT_READ)
        else:
            # если событие произошло не с серверным сокетом, то получить данные от клиента и отправить их обратно
            data = event_socket.recv(1024)
            print(f'Получены данные: {data}')
            event_socket.send(data)