from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...states import PostState
from ...utils.send_message import send_message
from ...utils.send_panel import send_panel


async def replace_links(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    chat_id = message.chat.id

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
