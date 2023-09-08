from aiogram.filters.callback_data import CallbackData


class BaseCallbackData(CallbackData, prefix='base'):
    action: str
    