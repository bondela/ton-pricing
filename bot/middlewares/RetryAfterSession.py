from asyncio import sleep
from typing import Optional

from aiogram import Bot
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.exceptions import (
    RestartingTelegram,
    TelegramRetryAfter,
    TelegramServerError,
)
from aiogram.methods.base import TelegramMethod, TelegramType
from icecream import ic


class RetryAfterSession(AiohttpSession):
    async def __call__(
            self,
            bot: Bot,
            method: TelegramMethod[TelegramType],
            chat_id: int = None,
            timeout: Optional[int] = None
    ) -> TelegramType:
        while True:
            try:
                return await super().make_request(bot, method, timeout)

            except (TelegramRetryAfter, RestartingTelegram, TelegramServerError) as e:
                ic(e.retry_after)
                await sleep(e.retry_after)
                continue

            except Exception as exception:
                ic(exception)
                if "message is not modified" in str(exception):
                    return False


            return