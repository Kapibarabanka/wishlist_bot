from main import bot, dp
from aiogram.types import Message
from config import admin_id
from aiogram.dispatcher.storage import FSMContext
from states import CurrentLists


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал: {message.text}"
    await message.reply(text=text)