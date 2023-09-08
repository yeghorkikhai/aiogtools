from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from aiotools_editor.utils.send_panel import send_panel


async def media_spoiler_switch(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()

    await state.update_data({
        "has_spoiler": not state_data.get('has_spoiler')
    })

    await callback_query.message.delete()

    await callback_query.answer(
        text=f"Спойлер {'увімкнено' if not state_data.get('has_spoiler') else 'вимкнено'}"
    )

    await send_panel(
        chat_id=callback_query.message.chat.id,
        state=state,
        bot=bot
    )
