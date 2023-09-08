from aiogram.filters.callback_data import CallbackData


class ButtonCallbackData(CallbackData, prefix='button'):
    action: str
    col: int
    row: int
