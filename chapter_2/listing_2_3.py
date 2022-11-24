import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1

res = asyncio.run(coroutine_add_one(number=1))

print(res)
