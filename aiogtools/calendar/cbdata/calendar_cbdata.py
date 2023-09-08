from aiogram.filters.callback_data import CallbackData
from datetime import date


class CalendarCallbackData(CallbackData, prefix='calendar'):
    action: str
    date: date
