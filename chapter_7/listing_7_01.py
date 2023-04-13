"""Многопоточный эхо-сервер"""
from threading import Thread
import socket


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f'Получено {data}, отправляю!')
        client.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    while True:
        conn, _ = server.accept() # блокируется в ожидании клиентов
        thread = Thread(target=echo, args=(conn, )) # как только клиент подключился, создать поток для выполнения
        # thread.daemon = True сделать поток демон, который будет завершаться вместе с главным потоком по ctrl+c
        thread.start() # начать выполнение потока