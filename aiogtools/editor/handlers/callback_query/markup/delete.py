from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....utils.refresh import refresh


async def delete_markup(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    chat_id = callback_query.message.chat.id

    await state.update_data({
        "markup": None
    })

    await refresh(chat_id=chat_id, state=state, bot=bot)
