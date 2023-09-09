from aiogram import Bot
from aiogram.fsm.context import FSMContext

from ..states import PostState
from ..enums import AllowedMethods, MediaPosition
from ..utils.send_message import send_message
from ..utils.send_panel import send_panel


async def create_post(
        state: FSMContext,
        back_callback_data: str,
        then_callback_data: str,
        back_title: str | None = None,
        then_title: str | None = None,
        allowed_methods: list[AllowedMethods] | None = None,
):
    await state.set_state(PostState.message)

    await state.update_data({
        "back_title": back_title,
        "then_title": then_title,
        "back_callback_data": back_callback_data,
        "then_callback_data": then_callback_data,
        "allowed_methods": allowed_methods
    })


async def edit_post(
        chat_id: int,
        state: FSMContext,
        bot: Bot,
        back_callback_data: str,
        then_callback_data: str,
        text: str | None = None,
        caption: str | None = None,
        photo: str | None = None,
        animation: str | None = None,
        video: str | None = None,
        video_note: str | None = None,
        audio: str | None = None,
        voice: str | None = None,
        document: str | None = None,
        album: list[tuple[str, str]] | None = None,
        markup: list[list[dict]] | None = None,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        has_media_spoiler: bool = False,
        back_title: str | None = None,
        then_title: str | None = None,
        allowed_methods: list[AllowedMethods] | None = None
):
    await state.set_state(PostState.edit)

    data = {
        "text": text,
        "caption": caption,
        "photo": photo,
        "animation": animation,
        "video": video,
        "video_note": video_note,
        "audio": audio,
        "voice": voice,
        "document": document,
        "album": album,
        "markup": markup,
        "disable_web_page_preview": disable_web_page_preview,
        "disable_notification": disable_notification,
        "has_media_spoiler": has_media_spoiler,
        "media_position": MediaPosition.UP,
        "back_title": back_title,
        "then_title": then_title,
        "back_callback_data": back_callback_data,
        "then_callback_data": then_callback_data,
        "allowed_methods": allowed_methods
    }

    await state.update_data(**data)

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
