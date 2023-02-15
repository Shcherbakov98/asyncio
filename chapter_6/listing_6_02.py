"""Создание пула процессов"""
from multiprocessing import Pool

def say_hello(name: str) -> str:
    return f'Привет, {name}'

if __name__ == '__main__':
    with Pool() as process_pool: # создать пул процессов
        # выполнить функцию say_hello в отдельных процессах и получить результат
        hi_jeff = process_pool.apply(say_hello, args=('jeff', ))
        hi_john = process_pool.apply(say_hello, args=('john', ))

        print(hi_jeff)
        print(hi_john)
