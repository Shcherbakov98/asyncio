"""Однопоточная модель MapReduce"""
import functools
from typing import Dict
from collections import defaultdict, Counter


def map_frequency(text: str) -> Dict[str, int]:
    words = text.split(' ')
    frequencies = dict()
    # frequencies = defaultdict(int)  # метод подсчета через defaultdict
    # frequencies = Counter(words)  # метод подсчета через Counter
    for word in words:
        # frequencies[word] += 1

        # стандартный метод подсчета
        if word in frequencies:
            # если слово уже есть в словаре частот прибавить 1
            frequencies[word] = frequencies[word] + 1
        else:
            # если слова еще нет в словаре частот, счетчик равен 1
            frequencies[word] = 1
    return frequencies


def merge_dict(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            # если слово встречается в обоих словарях, сложить счетчики
            merged[key] = merged[key] + second[key]
        else:
            # если слово не встречается в обоих словарях, скопировать счетчик
            merged[key] = second[key]
    return merged


lines = ["I know what I know",
         "I know that I know",
         "I don`t know much",
         "They don`t know much"]

mapped_result = [map_frequency(line) for line in lines] # для каждой строки текста выполнить операцию map

print('Mapped result:')
for result in mapped_result:
    print(result)

# редуцировать (свести) все промежуточные счетчики в окончательный результат
print('Final result:')
print(functools.reduce(merge_dict, mapped_result))