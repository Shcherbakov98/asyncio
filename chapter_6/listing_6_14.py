"""Наблюдение за ходом отображения"""
import asyncio
from concurrent.futures import ProcessPoolExecutor
import functools
import time
from multiprocessing import Value
from typing import Dict, List
from collections import defaultdict
from chapter_6.listing_6_08 import merge_dict


map_progres : Value


def init(progress: Value):
    global map_progres
    map_progres = progress


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = defaultdict(int)
    for line in chunk:
        word, _, count, _ = line.split('\t')
        counter[word] += int(count)

    with map_progres.get_lock():
        map_progres.value += 1

    return counter


async def progress_reporter(total_partitions: int):
    while map_progres.value < total_partitions:
        print(f'Завершено операций отображения: {map_progres.value / total_partitions * 100}%')
        await asyncio.sleep(1)

async def get_count_line_in_file():
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        s = sum(1 for _ in f)
    return s

async def main(partition_size: int):
    global map_progres
    count_line_file = await get_count_line_in_file()
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        chunk, c = [], 0
        loop = asyncio.get_running_loop()
        tasks = []
        map_progres = Value('i', 0)
        start = time.time()
        with ProcessPoolExecutor(initializer=init, initargs=(map_progres,)) as pool:
            total_partitions = count_line_file // partition_size
            print(total_partitions)
            reporter = asyncio.create_task(progress_reporter(total_partitions))
            for line in f:
                c += 1
                if c % partition_size == 0:
                    tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))
                    chunk = []
                else:
                    chunk.append(line)
            else:
                if chunk:
                    tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

            counters = await asyncio.gather(*tasks)

            await reporter

            final_result = functools.reduce(merge_dict, counters)
            print(f"Aardvark встречается {final_result['Aardvark']} раз.")
            end = time.time()
            print(f'Время MapReduce: {(end - start):.4f} секунд')


if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))
