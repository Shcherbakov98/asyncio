"""Чтение из стандартного ввода по одному символу"""
import sys
from asyncio import StreamReader
from collections import deque
from chapter_8.listing_8_07 import move_back_one_char, clear_line


async def read_line(stdin_reader: StreamReader) -> str:
    # функция удаления предыдущего символа из стандартного вывода
    def erase_last_char():
        move_back_one_char()
        sys.stdout.write(' ')
        move_back_one_char()

    delete_char = b'\x7f'  # символ забоя
    input_buffer = deque()
    while (input_char := await stdin_reader.read(1)) != b'\n':
        # если введен символ забоя, то удалить предыдущий символ
        if input_char == delete_char:
            if len(input_buffer) > 0:
                input_buffer.pop()
                erase_last_char()
                sys.stdout.flush()
        else:
            # все символы, кроме забоя, добавляются в конец буфера и эхо-копируются
            input_buffer.append(input_char)
            sys.stdout.write(input_char.decode())
            sys.stdout.flush()
    clear_line()
    return b"".join(input_buffer).decode()
