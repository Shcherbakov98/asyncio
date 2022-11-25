import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} c')
    await asyncio.sleep(delay=delay_seconds)
    print(f'сон в течении {delay_seconds} c закончен')
    return delay_seconds
