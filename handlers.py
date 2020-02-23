from main import bot, dp
from aiogram.types import Message
from config import admin_id
from aiogram.dispatcher.storage import FSMContext
from states import ChooseMode, CurrentLists
from CurrentList import default_list, CurrentList

START_MESSAGE = "Бот запущен"
current_list_key = 'current_list'


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text=START_MESSAGE)


@dp.message_handler(commands=["my_list"])
async def show_list(message: Message, state: FSMContext):
    data = await state.get_data()
    current_list = data.get(current_list_key)
    if current_list is None:
        current_list = default_list
        await state.update_data(current_list=current_list)
    await message.answer(str(current_list))
    await CurrentLists.Show.set()


@dp.message_handler(state=CurrentLists.Show, commands=["add"])
async def add_item_request(message: Message):
    text = f"Введите название подарка"
    await message.answer(text)
    await CurrentLists.AddItem.set()


@dp.message_handler(state=CurrentLists.AddItem)
async def add_item(message: Message, state: FSMContext):
    data = await state.get_data()
    current_list = data[current_list_key]
    current_list.add_item(message.text)
    await state.update_data(current_list=current_list)
    await message.answer(data[current_list_key])
    await CurrentLists.Show.set()


@dp.message_handler(state=CurrentLists.Show, commands=["remove"])
async def remove_item_request(message: Message):
    text = f"Введите номер подарка"
    await message.answer(text)
    await CurrentLists.RemoveItem.set()


@dp.message_handler(state=CurrentLists.RemoveItem)
async def remove_item(message: Message, state: FSMContext):
    data = await state.get_data()
    current_list = data[current_list_key]
    current_list.remove_item(int(message.text))
    await state.update_data(current_list=current_list)
    await message.answer(data[current_list_key])
    await CurrentLists.Show.set()

