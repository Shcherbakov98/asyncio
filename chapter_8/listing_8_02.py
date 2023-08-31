"""Использование протокола"""
import asyncio
from asyncio import AbstractEventLoop
from chapter_8.listing_8_01 import HTTPGetClientProtocol


async def make_request(host: str, port: int, loop: AbstractEventLoop):
    def protocol_factory():
        return HTTPGetClientProtocol(host, loop)

    _, protocol = await loop.create_connection(protocol_factory, host=host, port=port)

    return await protocol.get_response()


async def main():
    loop = asyncio.get_running_loop()
    result = await make_request('ya.ru', 80, loop)
    print('result!!!', result)


asyncio.run(main())
