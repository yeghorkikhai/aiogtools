from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...enums import MediaPosition
from ...states import PostState
from ...utils.send_message import send_message
from ...utils.send_panel import send_panel
from ...utils.media import update_media, set_media
from ...utils.telegraph import Telegraph


async def parse_media(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    chat_id = message.chat.id
    state_name = await state.get_state()

    if state_name == "PostState:message":
        await set_media(state, message)
    elif state_name == "PostState:edit_media" or state_name == "PostState:edit":
        state_data = await state.get_data()
        file_id = message.photo[-1].file_id

        if state_data.get("media_position") == MediaPosition.UP:
            await update_media(
                state=state,
                photo=file_id,
            )
            await state.update_data({
                "caption": state_data.get("text"),
                "text": None
            })
        elif state_data.get("media_position") == MediaPosition.DOWN:
            telegraph = Telegraph(bot=bot)
            media_url = await telegraph.upload_file_from_telegram(file_id=file_id)
            await state.update_data({
                "media_url": media_url
            })

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
