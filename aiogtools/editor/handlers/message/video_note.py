from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...enums import MediaPosition
from ...utils.media import set_media
from ...states import PostState
from ...utils.send_message import send_message
from ...utils.send_panel import send_panel


async def video_note(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    print("Video Note")

    chat_id = message.chat.id
    state_name = await state.get_state()

    if state_name == "PostState:message":
        await set_media(state, message)

    print(await state.get_data())

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
