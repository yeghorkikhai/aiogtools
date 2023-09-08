from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from aiotools_editor.utils.send_panel import send_panel


async def disable_web_page_preview_switch(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()

    await state.update_data({
        "disable_web_page_preview": not state_data.get('disable_web_page_preview')
    })

    state_data = await state.get_data()

    await callback_query.message.delete()

    await callback_query.answer(
        text=f"Превью {'увімкнено' if not state_data.get('disable_web_page_preview') else 'вимкнено'}"
    )

    await send_panel(
        chat_id=callback_query.message.chat.id,
        state=state,
        bot=bot
    )
