"""Чередование генераторов"""
from typing import Generator


def generator(start: int, end: int):
    for i in range(start, end):
        yield i


one_to_five = generator(1, 6)
five_to_ten = generator(5, 10)

# выполнить один шаг генератора
def run_generator_step(gen: Generator[int, None, None]):
    try:
        return gen.send(None)
    except StopIteration as si:
        # pass
        return si.value


# чередовать выполнение двух генераторов
while True:
    one_to_five_result = run_generator_step(one_to_five)
    five_to_ten_result = run_generator_step(five_to_ten)
    if one_to_five_result is None and five_to_ten_result is None:
        break
    print(one_to_five_result)
    print(five_to_ten_result)