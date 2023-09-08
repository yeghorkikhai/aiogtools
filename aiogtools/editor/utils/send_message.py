from aiogram import Bot
from aiogram.fsm.context import FSMContext


async def send_message(
        chat_id: int,
        bot: Bot,
        state: FSMContext
):
    state_data = await state.get_data()

    if "text" in state_data:
        message = await bot.send_message(
            chat_id=chat_id,
            text=state_data.get("text"),
            disable_notification=state_data.get("disable_notification"),
            disable_web_page_preview=state_data.get("disable_web_page_preview")
        )
    elif "photo" in state_data:
        message = await bot.send_photo(
            chat_id=chat_id,
            photo=state_data.get("photo")
        )
    elif "animation" in state_data:
        message = await bot.send_animation(
            chat_id=chat_id,
            animation=state_data.get("animation")
        )
    elif "video" in state_data:
        message = await bot.send_video(
            chat_id=chat_id,
            video=state_data.get("video")
        )
    else:
        return None

    await state.update_data({
        "pre_message_id": message.message_id
    })
