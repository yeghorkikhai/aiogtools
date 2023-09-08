from aiogram.fsm.state import StatesGroup, State


class PostState(StatesGroup):
    message = State()

    edit = State()

    edit_text = State()

    edit_markup = State()
    edit_button = State()
    edit_button_name = State()
    edit_button_url = State()

    edit_media = State()

    replace_links = State()
