import asyncio


async def add_one(num: int) -> int:
    return num + 1


async def main() -> None:
    one_plus_one = await add_one(1)  # приостановиться и ждать результат
    two_plus_one = await add_one(2)  # приостановиться и ждать результат
    print(one_plus_one)
    print(two_plus_one)

asyncio.run(main())
