from aiogram import Bot
from aiogram.fsm.context import FSMContext

from .media import build_media


async def send_message(
        chat_id: int,
        bot: Bot,
        state: FSMContext
):
    state_data = await state.get_data()

    print(state_data)

    if state_data.get("text") is not None:
        message = await bot.send_message(
            chat_id=chat_id,
            text=state_data.get("text"),
            disable_notification=state_data.get("disable_notification"),
            disable_web_page_preview=state_data.get("disable_web_page_preview")
        )
    elif state_data.get("photo") is not None:
        message = await bot.send_photo(
            chat_id=chat_id,
            photo=state_data.get("photo"),
            caption=state_data.get("caption"),
            disable_notification=state_data.get("disable_notification"),
            has_spoiler=state_data.get("has_media_spoiler")
        )
    elif state_data.get("animation") is not None:
        message = await bot.send_animation(
            chat_id=chat_id,
            animation=state_data.get("animation"),
            caption=state_data.get("caption"),
            disable_notification=state_data.get("disable_notification"),
            has_spoiler=state_data.get("has_media_spoiler")
        )
    elif state_data.get("video") is not None:
        message = await bot.send_video(
            chat_id=chat_id,
            video=state_data.get("video"),
            caption=state_data.get("caption"),
            disable_notification=state_data.get("disable_notification"),
            has_spoiler=state_data.get("has_media_spoiler")
        )
    elif state_data.get("video_note") is not None:
        message = await bot.send_video_note(
            chat_id=chat_id,
            video_note=state_data.get("video_note"),
            disable_notification=state_data.get("disable_notification")
        )
    elif state_data.get("audio") is not None:
        message = await bot.send_audio(
            chat_id=chat_id,
            audio=state_data.get("audio"),
            caption=state_data.get("caption"),
            disable_notification=state_data.get("disable_notification")
        )
    elif state_data.get("voice") is not None:
        message = await bot.send_voice(
            chat_id=chat_id,
            voice=state_data.get("voice"),
            disable_notification=state_data.get("disable_notification")
        )
    elif state_data.get("document") is not None:
        message = await bot.send_document(
            chat_id=chat_id,
            document=state_data.get("document"),
            disable_notification=state_data.get("disable_notification")
        )
    elif state_data.get("album") is not None:
        media = await build_media(state)
        album = await bot.send_media_group(
            chat_id=chat_id,
            media=media
        )
    else:
        return

    if state_data.get("album") is None:
        await state.update_data({
            "pre_message_id": message.message_id
        })

    if state_data.get("album") is not None:
        await state.update_data({
            "pre_message_id": [message.message_id for message in album]
        })
