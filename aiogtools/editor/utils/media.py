from aiogram.types import (
    Message,
    InputMedia,
    InputMediaPhoto,
    InputMediaAnimation,
    InputMediaVideo,
    InputMediaAudio,
    InputMediaDocument
)
from aiogram.fsm.context import FSMContext

from ..enums import MediaPosition


async def set_media(
        state: FSMContext,
        message: Message
):
    await state.update_data({
        "photo": message.photo[-1].file_id if message.photo else None,
        "animation": message.animation.file_id if message.animation else None,
        "video": message.video.file_id if message.video else None,
        "video_note": message.video_note.file_id if message.video_note else None,
        "audio": message.audio.file_id if message.audio else None,
        "voice": message.voice.file_id if message.voice else None,
        "document": message.document.file_id if message.document else None,
        "caption": message.html_text,
        "markup": message.reply_markup.model_dump_json() if message.reply_markup else None,
        "media_position": MediaPosition.UP,
        "has_media_spoiler": message.has_media_spoiler
    })


async def update_media(
        state: FSMContext,
        photo: str | None = None,
        animation: str | None = None,
        video: str | None = None,
        video_note: str | None = None,
        audio: str | None = None,
        voice: str | None = None,
        document: str | None = None,
        album: list[tuple[str, str]] | None = None
):
    await state.update_data({
        "photo": photo,
        "animation": animation,
        "video": video,
        "video_note": video_note,
        "audio": audio,
        "voice": voice,
        "document": document,
        "album": album
    })


async def parse_album(
        album: list[Message]
) -> list[tuple[str, str]]:
    media: list[tuple[str, str]] = []

    for message in album:
        if message.photo:
            media.append(("photo", message.photo[-1].file_id))
        elif message.animation:
            media.append(("animation", message.animation.file_id))
        elif message.video:
            media.append(("video", message.video.file_id))
        elif message.audio:
            media.append(("audio", message.audio.file_id))
        elif message.document:
            media.append(("document", message.document.file_id))
        else:
            continue

    return media


async def build_media(
        state: FSMContext,
) -> list[
    InputMediaPhoto |
    InputMediaAnimation |
    InputMediaVideo |
    InputMediaAudio |
    InputMediaDocument
]:
    media = []
    data = await state.get_data()
    album: list[tuple[str, str]] = data.get("album")

    for index, item in enumerate(album):
        media_type, media_id = item
        match media_type:
            case "photo":
                media.append(
                    InputMediaPhoto(
                        media=media_id,
                        caption=data.get("caption") if index < 1 else None,
                        has_spoiler=data.get("has_media_spoiler")
                    )
                )
            case "animation":
                media.append(
                    InputMediaAnimation(
                        media=media_id,
                        caption=data.get("caption") if index < 1 else None,
                        has_spoiler=data.get("has_media_spoiler")
                    )
                )
            case "video":
                media.append(
                    InputMediaVideo(
                        media=media_id,
                        caption=data.get("caption") if index < 1 else None,
                        has_spoiler=data.get("has_media_spoiler")
                    )
                )
            case "audio":
                media.append(
                    InputMediaAudio(
                        media=media_id,
                        caption=data.get("caption") if index < 1 else None,
                    )
                )
            case "document":
                media.append(
                    InputMediaDocument(
                        media=media_id,
                        caption=data.get("caption") if index < 1 else None,
                    )
                )
            case _:
                pass

    return media
