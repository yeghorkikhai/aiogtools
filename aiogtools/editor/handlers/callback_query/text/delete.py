from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext


from ....utils.refresh import refresh


async def delete_text(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    chat_id = callback_query.message.chat.id
    state_data = await state.get_data()

    if state_data.get('text') is not None:
        await state.update_data({
            "text": None
        })
    else:
        await state.update_data({
            "caption": None
        })

    await refresh(chat_id=chat_id, state=state, bot=bot)
