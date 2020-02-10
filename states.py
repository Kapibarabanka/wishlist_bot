from aiogram.dispatcher.filters.state import StatesGroup, State


class CurrentLists(StatesGroup):
    Add = State()
    Surname = State()
    DOB = State()
    City = State()