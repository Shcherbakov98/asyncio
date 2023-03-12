"""Распараллеливание с помощью MapReduce и пула процессов"""
import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List
from collections import defaultdict


def partition(data: List, chunk_size: int) -> List:
    """Разбивает на n частей data размером chunk_size"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    """Итерируюясь по чанку, увеличивает счетчик вхождения каждого слова"""
    counter = defaultdict(int)
    for line in chunk:
        word, _, count, _ = line.split('\t')
        counter[word] += int(count)

    return counter


def merge_dict(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    """Объединяет результаты двух словарей возвращая третий"""
    merged = first
    for key in second:
        merged[key] += second[key] # т.к defaultdict
        # if key in merged:
        #     merged[key] = merged[key] + second[key]
        # else:
        #     merged[key] = second[key]

    return merged

async def main(partition_size: int):
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        chunk, c = [], 0
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for line in f:
                c += 1
                if c % partition_size == 0:
                    tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))
                    chunk = []
                else:
                    chunk.append(line)

            # for chunk in partition(contents, chunk_size=partition_size):
            #     tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            intermediate_result = await asyncio.gather(*tasks)
            final_result = functools.reduce(merge_dict, intermediate_result)
            print(f"Aardvark встречается {final_result['Aardvark']} раз.")
            end = time.time()
            print(f'Время MapReduce: {(end - start):.4f} секунд')



if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))