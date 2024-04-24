from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from icecream import ic


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        callback = data["handler"].callback
        user = f"{event.from_user.username or event.from_user.full_name} | {event.from_user.id}"
        date = str(datetime.now().replace(microsecond=0))
        ic(callback, user, date)
        return await handler(event, data)
