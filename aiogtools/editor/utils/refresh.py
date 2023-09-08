from aiogram import Bot
from aiogram.fsm.context import FSMContext

from .send_message import send_message
from .send_panel import send_panel


async def refresh(
        chat_id: int,
        state: FSMContext,
        bot: Bot
):
    data = await state.get_data()

    await bot.delete_message(
        chat_id=chat_id,
        message_id=data.get("editor_message_id")
    )

    if data.get("album") is None:
        await bot.delete_message(
            chat_id=chat_id,
            message_id=data.get("pre_message_id")
        )
    else:
        for message_id in data.get("pre_message_id"):
            await bot.delete_message(
                chat_id=chat_id,
                message_id=message_id
            )

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
