"""Подсчет частот слов, начинающихся с буквой 'а'"""
import time
from collections import defaultdict

freq = defaultdict(int)

with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as file:
    start = time.time()
    for l in file:
        data = l.strip().split('\t')
        word = data[0]
        count = int(data[2])
        freq[word] += count

    end = time.time()
    print(f'Total time: {end - start:.4f}')

# 87 секунд