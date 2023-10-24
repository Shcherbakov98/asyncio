"""Клиент чат-сервера"""
import asyncio
import os
import logging
import tty
from asyncio import StreamReader, StreamWriter
from collections import deque
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from chapter_8.listing_8_05 import create_stdin_reader
from chapter_8.listing_8_07 import *
from chapter_8.listing_8_08 import read_line
from chapter_8.listing_8_09 import MessageStore


async def send_message(message: str, writer: StreamWriter):
    writer.write((message + '\n').encode())
    await writer.drain()


# прослушивать сообщения от сервера и добавлять их в хранилище
async def listen_for_messages(reader: StreamReader, message_store: MessageStore):
    while (message := await reader.readline()) != b'':
        await message_store.append(message.decode())
    await message_store.append('Сервер закрыл соединение.')


# читать данные введенные пользователем и отправлять их серверу
async def read_and_send(stdin_reader: StreamReader, writer: StreamWriter):
    while True:
        message = await read_line(stdin_reader)
        await send_message(message, writer)


async def main():
    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            sys.stdout.write(item)
        restore_cursor_position()

    tty.setcbreak(0)
    os.system('clear')
    stdin_reader = await create_stdin_reader()
    sys.stdout.write('Введите имя пользователя: ')
    username = await read_line(stdin_reader)
    os.system('clear')
    rows = move_to_bottom_of_screen()
    messages = MessageStore(redraw_output, rows - 1)

    # подключится к серверу и отправить сообщение CONNECT с именем пользователя
    reader, writer = await asyncio.open_connection('127.0.0.1', 8000)

    writer.write(f'CONNECT {username}\n'.encode())
    await writer.drain()

    # создать задачи на прослушивание и ввода данных и ждать, пока какая-то из них завершится
    messages_listener = asyncio.create_task(listen_for_messages(reader, messages))
    input_listener = asyncio.create_task(read_and_send(stdin_reader, writer))

    try:
        await asyncio.wait([messages_listener, input_listener], return_when=asyncio.FIRST_COMPLETED)
    except Exception as e:
        logging.exception(e)
        writer.close()
        await writer.wait_closed()

asyncio.run(main())
