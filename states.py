from aiogram.dispatcher.filters.state import StatesGroup, State


class ChooseMode(StatesGroup):
    CurrentLists = StatesGroup()
    OtherLists = StatesGroup()


# Manage list of the current user
class CurrentLists(StatesGroup):
    Show = State()
    Edit = State()
    EditItem = State()
    AddItem = State()
    RemoveItem = State()


# Explore lists of other users
class OtherLists(StatesGroup):
    Find = State()
