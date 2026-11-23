# база
import asyncio
import logging

# Зависимости
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Зависимости от созданных файлов
from Routers import router as start_router
from loader import gettoken, getid
from timer import scheduler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
)

log = logging.getLogger("bot")

dp = Dispatcher()

TOKEN = gettoken()
DEV = getid()


async def on_startup(bot: Bot) -> None:
    await bot.send_message(chat_id=DEV, text="Готов к работе!")


async def main():
    scheduler.start()
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
