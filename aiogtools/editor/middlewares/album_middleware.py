import asyncio
from typing import Union, Callable, Any, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


class AlbumMiddleware(BaseMiddleware):
    album_data: dict = {}
    dd = False

    def __init__(self, latency: Union[int, float] = 0.01):
        self.latency = latency
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        if not event.media_group_id:
            return await handler(event, data)
        try:
            self.album_data[event.media_group_id].append(event)
            return
        except KeyError:
            self.album_data[event.media_group_id] = [event]
            await asyncio.sleep(1)

            data["album"] = self.album_data[event.media_group_id]

            del self.album_data[event.media_group_id]

            return await handler(event, data)
