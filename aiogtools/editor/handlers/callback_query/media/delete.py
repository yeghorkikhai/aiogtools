from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext


async def delete_media(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    pass
