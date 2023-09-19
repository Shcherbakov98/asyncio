"""Приложение для асинхронной задержки"""
import asyncio
import os
import sys
import tty
from collections import deque
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from chapter_8.listing_8_05 import create_stdin_reader
from chapter_8.listing_8_07 import *
from chapter_8.listing_8_08 import read_line
from chapter_8.listing_8_09 import MessageStore


async def sleep(delay: int, message_store: MessageStore):
    # добавить выходные сообщения в хранилище
    await message_store.append(f'Начало задержки {delay}')
    await asyncio.sleep(delay)
    await message_store.append(f'Конец задержки {delay}')


async def main():
    tty.setcbreak(sys.stdin)
    os.system('clear')
    rows = move_to_bottom_of_screen()

    # обратный вызов, который перемещает курсор в начало экрана, перерисовывает экран и возвращает курсор обратно
    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(callback=redraw_output, max_size=rows - 1)

    stdin_reader = await create_stdin_reader()

    while True:
        line = await read_line(stdin_reader=stdin_reader)
        delay_time = int(line)
        asyncio.create_task(sleep(delay_time, messages))

asyncio.run(main())
