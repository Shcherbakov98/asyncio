"""Более сложная программа echo"""
from random import randrange
import time


user_input = ''

while user_input != 'quit':
    user_input = input('Введите текст: ')
    for i in range(randrange(10)):
        time.sleep(.5)
        print(user_input)