from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from aiotools_editor.cbdata import ButtonCallbackData


async def edit_url(
        callback_query: CallbackQuery,
        callback_data: ButtonCallbackData,
        state: FSMContext
):
    pass
