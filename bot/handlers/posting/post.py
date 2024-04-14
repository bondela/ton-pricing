import os
from datetime import datetime
from typing import Any

from aiogram import Bot
from icecream import ic
from .api import get_exchange


async def scheduled_post(bot: Bot = None) -> Any:
    """
    Sends a message with current TON exchange rate in different currencies and up/down percents
    :param bot:
    :return:
    """

    response = await get_exchange()
    if not isinstance(response, dict):
        ic(response)
        return

    ton_usd = response.get("rates", {}).get("TON", {}).get("prices", {}).get("USD", {}) or 0
    ton_rub = response.get("rates", {}).get("TON", {}).get("prices", {}).get("RUB", {}) or 0

    diff_day = response.get("rates", {}).get("TON", {}).get("diff_24h", {}).get("USD", {}) or 0
    diff_week = response.get("rates", {}).get("TON", {}).get("diff_7d", {}).get("USD", {}) or 0
    diff_month = response.get("rates", {}).get("TON", {}).get("diff_30d", {}).get("USD", {}) or 0

    # TODO: Use redis. Post message every 5 minutes, update message (edit) with actual information every 30 seconds.

    await bot.send_message(chat_id=config.channel_id, text=f"<b>🇺🇸 ${round(ton_usd, 2)} ~ 🇷🇺{round(ton_rub, 2)}₽\n\n"
                                                           f"Last 24h: <code>{diff_day}</code>\n"
                                                           f"Last week: <code>{diff_week}</code>\n"
                                                           f"Last month: <code>{diff_month}</code></b>")
