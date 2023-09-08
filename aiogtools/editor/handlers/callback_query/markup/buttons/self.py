from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .....cbdata import ButtonCallbackData


async def self(
        callback_query: CallbackQuery,
        callback_data: ButtonCallbackData,
        state: FSMContext
):
    pass
