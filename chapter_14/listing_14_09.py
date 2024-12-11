"""Использование объекта CustomFuture в цикле"""
from listing_14_08 import CustomFuture


future = CustomFuture()
i = 0
while True:
    try:
        print('Проверяется будущий объект...')
        gen = future.__await__()
        gen.send(None)
        print('Будущий объект не готов...')
        if i == 2:
            print('Устанавливаются значения будущего объекта...')
            future.set_result('Готово!')
        i += 1
    except StopIteration as si:
        print(f'Значение равно: {si.value}')
        break
