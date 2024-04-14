import os
from asyncio import run

from aiocron import crontab
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.posting.post import scheduled_post
from middlewares.RetryAfterSession import RetryAfterSession
from config_reader import config

from icecream import ic


async def setup_handlers(dp: Dispatcher) -> None:
    # for router in await routers_collector():
    #     dp.include_router(router)
    pass


async def setup_database() -> None:
    # await run_database()
    pass


async def setup_middlewares(dp: Dispatcher) -> None:
    # TODO: Middleware for logging (icecream)
    # TODO: Middleware for database pool
    # dp.message.middleware.register()
    pass


async def setup_crontabs(bot: Bot) -> None:
    # TODO: Write a crontabs for scheduled price parsing and posting in channel
    crontab('* * * * *', func=scheduled_post, args=(bot,), start=True)
    pass


async def main() -> None:
    # TODO: Create a custom session to bypass RetryAfter exception
    bot = Bot(token=config.bot_token.get_secret_value(),
              session=RetryAfterSession(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True))

    dp: Dispatcher = Dispatcher(storage=MemoryStorage())

    await setup_handlers(dp=dp)
    await setup_crontabs(bot=bot)

    ic("💩")
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())
