from aiogram import Router
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message):
    await message.answer("Привет! Я бот для задач.")


@router.message(Command("help"))
async def cmd_help(message):
    await message.answer("Список команд: /start, /help")
