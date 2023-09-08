from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...enums import MediaPosition
from ...states import PostState
from ...utils.send_message import send_message
from ...utils.send_panel import send_panel
from ...utils.media import update_media


async def photo(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    chat_id = message.chat.id
    state_name = await state.get_state()

    if state_name == "PostState:message":
        await state.update_data({
            "photo": message.photo[-1].file_id,
            "caption": message.html_text,
            "markup": message.reply_markup.model_dump_json() if message.reply_markup else None,
            "media_position": MediaPosition.UP,
            "has_media_spoiler": message.has_media_spoiler
        })
    elif state == "PostState:edit_media":
        state_data = await state.get_data()

        if state_data.get("media_position") == MediaPosition.UP:
            await update_media(
                state=state,
                photo=message.photo[-1].file_id
            )
        elif state_data.get("media_position") == MediaPosition.DOWN:
            pass

    await send_message(
        chat_id=chat_id,
        state=state,
        bot=bot
    )

    await send_panel(
        chat_id=chat_id,
        state=state,
        bot=bot
    )

    await state.set_state(PostState.edit)
