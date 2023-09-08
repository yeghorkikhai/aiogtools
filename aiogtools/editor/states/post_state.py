from aiogram.fsm.state import StatesGroup, State


class PostState(StatesGroup):
    message = State()

    edit = State()

    edit_text = State()
    edit_markup = State()
    edit_media = State()
