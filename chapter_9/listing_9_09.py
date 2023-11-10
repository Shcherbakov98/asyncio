"""Оконечная точка типа WebSocket в Starlette"""
import asyncio
import typing

from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket


class UserCounter(WebSocketEndpoint):
    encoding = 'text'
    sockets = []

    # когда клиент подключается, добавить его в список сокетов и сообщить остальным новое значение счетчика
    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        UserCounter.sockets.append(websocket)
        await self._send_count()

    # когда клиент отключается, удалить его из списка и сообщить остальным новое значение счетчика
    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        UserCounter.sockets.remove(websocket)
        await self._send_count()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        pass

    # сообщить всем клиентам, сколько пользователей сейчас подключено
    # в случае исключения, удалить соответствующего клиента из списка
    async def _send_count(self):
        if len(UserCounter.sockets) > 0:
            count_str = str(len(UserCounter.sockets))
            task_to_socket = {
                asyncio.create_task(websocket.send_text(count_str)): websocket for websocket in UserCounter.sockets
            }

            done, pending = await asyncio.wait(task_to_socket)
            for task in done:
                if task.exception() is not None:
                    if task_to_socket[task] in UserCounter.sockets:
                        UserCounter.sockets.remove(task_to_socket[task])


app = Starlette(routes=[WebSocketRoute('/counter', UserCounter)])
