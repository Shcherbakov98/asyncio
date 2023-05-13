"""Взаимоблокировки"""
from threading import Lock, Thread
import time


lock_a = Lock()
lock_b = Lock()


def a():
    # захватить блокировку А
    with lock_a:
        print('Захвачена блокировка а из метода а')
        time.sleep(.5)  # ждать 1 сек (условия для взаимоблокировки)
        with lock_b:
            print('Захвачены обе блокировки из метода а!')


def b():
    # захватить блокировку B
    with lock_a:
        print('Захвачена блокировка b из метода b')
        with lock_b:
            print('Захвачены обе блокировки из метода b!')


thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

