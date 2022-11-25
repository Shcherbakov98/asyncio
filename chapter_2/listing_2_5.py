import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(delay=1)  # приостановить на 1 с
    return 'Hello, world!'


async def main() -> None:
    message = await hello_world_message()  # приостановить main до завершения hello_world_message
    print(message)

asyncio.run(main())
