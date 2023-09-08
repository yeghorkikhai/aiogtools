from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ...utils.send_panel import send_panel


async def panel(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    await callback_query.message.delete()

    await send_panel(
        chat_id=callback_query.message.chat.id,
        state=state,
        bot=bot
    )
