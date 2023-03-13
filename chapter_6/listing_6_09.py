"""Распараллеливание операции reduce"""
import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List
from chapter_6.listing_6_08 import partition, merge_dict, map_frequencies


async def reduce(loop, pool, counters, chunk_size) -> Dict[str, int]:
    # разбить словари на допускающие распараллеливание порции размером chunk_size
    chunks: List[List[Dict]] = list(partition(counters, chunk_size))
    reducers = []
    while len(chunks[0]) > 1:
        for chunk in chunks:
            # редуцировать каждую порцию в один словарь
            reducer = functools.partial(functools.reduce, merge_dict, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))

        # ждать завершение всех операций редукции
        reducer_chunks = await asyncio.gather(*reducers)
        # снова разбить результаты и выполнить еще одну итерацию цикла
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()
    return chunks[0][0]

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
            final_result = await reduce(loop, pool, intermediate_result, 1000)
            # final_result = functools.reduce(merge_dict, intermediate_result)

            print(f"Aardvark встречается {final_result['Aardvark']} раз.")

            end = time.time()
            print(f'Время MapReduce: {(end - start):.4f} секунд')



if __name__ == "__main__":
    asyncio.run(main(partition_size=60000))