from datetime import datetime
from typing import Any

from aiogram import Bot
from icecream import ic
from .api import get_exchange


async def scheduled_post(bot: Bot = None) -> Any:
    ic()
    response = await get_exchange()
    if not isinstance(response, dict):
        return

    ton_usd = response.get("rates", {}).get("TON", {}).get("prices", {}).get("USD", {}) or 0
    ton_rub = response.get("rates", {}).get("TON", {}).get("prices", {}).get("RUB", {}) or 0

    diff_day = response.get("rates", {}).get("TON", {}).get("diff_24h", {}).get("USD", {}) or 0
    diff_week = response.get("rates", {}).get("TON", {}).get("diff_7d", {}).get("USD", {}) or 0
    diff_month = response.get("rates", {}).get("TON", {}).get("diff_30d", {}).get("USD", {}) or 0

    await bot.send_message(chat_id=419675195, text=f"<b>🇺🇸 ${round(ton_usd, 2)} ~ 🇷🇺{round(ton_rub, 2)}₽\n\n"
                                                   f"Last 24h: <code>{diff_day}</code>\n"
                                                   f"Last week: <code>{diff_week}</code>\n"
                                                   f"Last month: <code>{diff_month}</code></b>")
