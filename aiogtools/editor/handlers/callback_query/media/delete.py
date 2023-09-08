from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....utils.refresh import refresh


async def delete_media(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    chat_id = callback_query.message.chat.id
    state_data = await state.get_data()

    if state_data.get("album") is not None:
        pass
    else:
        await state.update_data({
            "text": state_data.get("caption"),
            "caption": None,
            "photo": None,
            "animation": None,
            "audio": None,
            "voice": None,
            "video": None,
            "video_note": None,
            "document": None,
            "has_media_spoiler": False
        })

    await refresh(chat_id=chat_id, state=state, bot=bot)
