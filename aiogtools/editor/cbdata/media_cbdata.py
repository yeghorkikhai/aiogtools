from aiogram.filters.callback_data import CallbackData
from ..enums import MediaPosition


class MediaCallbackData(CallbackData, prefix='media'):
    action: str
    position: MediaPosition
