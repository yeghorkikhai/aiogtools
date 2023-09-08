from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from aiotools_editor.utils.send_panel import send_panel


async def disable_notifications_switch(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()

    await state.update_data({
        "disable_notifications": not state_data.get('disable_notifications')
    })

    state_data = await state.get_data()

    await callback_query.message.delete()

    await callback_query.answer(
        text=f"Сповіщення {'увімкнено' if not state_data.get('disable_notifications') else 'вимкнено'}"
    )

    await send_panel(
        chat_id=callback_query.message.chat.id,
        state=state,
        bot=bot
    )

