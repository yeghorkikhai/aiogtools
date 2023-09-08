from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....utils.refresh import refresh


async def media_spoiler_switch(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()

    await state.update_data({
        "has_media_spoiler": not state_data.get('has_media_spoiler')
    })

    await callback_query.answer(
        text=f"Спойлер {'увімкнено' if not state_data.get('has_spoiler') else 'вимкнено'}"
    )

    chat_id = callback_query.message.chat.id

    await refresh(chat_id, state, bot)
