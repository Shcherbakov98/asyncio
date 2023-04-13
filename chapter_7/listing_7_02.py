"""Создание подкласса Thread для чистой остановки"""
from threading import Thread
import socket


class ClientEchoThread(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client

    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                # если нет данных, возбудить исключение, это бывает, когда подключение было закрыто клиентом,
                # или остановлено сервером
                if not data:
                    raise BrokenPipeError('Подключение закрыто!')
                print(f'Получено {data}, отправляю!')
                self.client.sendall(data)
        except OSError as e:
            # в случае исключения, выйти из метода run, при этом поток завершается
            print(f'Поток прерван исключением {e}, производится остановка!')

    def close(self):
        # разомкнуть подключение, если поток еще активен; поток может быть неактивен, если клиент закрыл подключение
        if self.is_alive():
            self.client.sendall(bytes('Останавливаюсь', encoding='utf-8'))
            # разомкнуть подключение клиента, остановив чтения и запись
            self.client.shutdown(socket.SHUT_RDWR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    conn_threads = []
    try:
        while True:
            conn, _ = server.accept()
            thread = ClientEchoThread(conn)
            conn_threads.append(thread)
            thread.start()
    except KeyboardInterrupt:
        print('Останавливаюсь!')
        # вызвать метод close созданных потомков, чтобы разомкнуть все клиентские подключения в случае прерывания
        [thread.close() for thread in conn_threads]