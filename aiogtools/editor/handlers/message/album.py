from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...enums import MediaPosition
from ...states import PostState
from ...utils.media import parse_album, set_media
from ...utils.send_message import send_message
from ...utils.send_panel import send_panel


async def get_album(
        message: Message,
        state: FSMContext,
        album: list[Message],
        bot: Bot
):
    chat_id = message.chat.id
    state_name = await state.get_state()

    if state_name == "PostState:message":
        media = await parse_album(album)

        await state.update_data({
            "album": media,
            "caption": album[0].caption,
            "media_position": MediaPosition.UP,
            "has_media_spoiler": album[0].has_media_spoiler
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
