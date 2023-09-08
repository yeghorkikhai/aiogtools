from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ...utils.send_message import send_message
from ...utils.send_panel import send_panel
from ...enums import MediaPosition
from ...states import PostState


async def text(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    chat_id = message.chat.id
    state_name = await state.get_state()

    if state_name == "PostState:message":
        await state.update_data({
            "text": message.html_text,
            "markup": message.reply_markup.model_dump_json() if message.reply_markup else None,
            "disable_web_page_preview": False,
            "disable_notification": False,
            "media_position": MediaPosition.UP
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
    elif state_name == "PostState:edit_text":

        state_data = await state.get_data()

        if state_data.get('text') is not None:
            await state.update_data({
                "text": message.html_text
            })
        else:
            await state.update_data({
                "caption": message.html_text
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
