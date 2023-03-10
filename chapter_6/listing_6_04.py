"""Исполнители пула процессов"""
import time
from concurrent.futures import ProcessPoolExecutor

def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f'Закончен подсчет до {count_to}, за время {end - start}')
    return counter


if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 3, 5, 22, 100000000]
        for result in process_pool.map(count, numbers):
            print(result)


# Закончен подсчет до 1, за время 2.384185791015625e-06
# Закончен подсчет до 3, за время 2.6226043701171875e-06
# Закончен подсчет до 5, за время 2.6226043701171875e-06
# Закончен подсчет до 22, за время 2.1457672119140625e-06
# 1
# 3
# 5
# 22
# Закончен подсчет до 100000000, за время 8.025124788284302
# 100000000