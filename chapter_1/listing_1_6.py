"""
Многопоточное вычисление последовательности чисел Фибоначчи
"""

import time
import threading


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n-1) + fib(n - 2)
    print(f'fib({number}) равно {fib(number)}')


def fibs_with_threading():
    fortieth_thread = threading.Thread(target=print_fib, args=(40, ))
    fortieth_first_thread = threading.Thread(target=print_fib, args=(41, ))

    fortieth_thread.start()
    fortieth_first_thread.start()

    fortieth_thread.join()
    fortieth_first_thread.join()


start_threads = time.time()
fibs_with_threading()
end_threads = time.time()

print(f'Время работы {end_threads - start_threads:.4f} c.')
