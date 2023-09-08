from aiogram import Router, F
from aiogram.filters import StateFilter

# Handlers
from .text import text
from .photo import photo
from .animation import animation
from .video import video
from .video_note import video_note
from .audio import audio
from .voice import voice
from .document import document
from .sticker import sticker
from .poll import poll
from .album import album

# States
from ...states import PostState


router = Router()

router.message.register(
    text,
    F.text,
    StateFilter(PostState.message & PostState.edit_text)
)
router.message.register(
    photo,
    F.photo,
    StateFilter(PostState.message)
)
router.message.register(
    animation,
    F.animation,
    StateFilter(PostState.message)
)
router.message.register(
    video,
    F.video,
    StateFilter(PostState.message)
)
router.message.register(
    video_note,
    F.video_note,
    StateFilter(PostState.message)
)
router.message.register(
    audio,
    F.audio,
    StateFilter(PostState.message)
)
router.message.register(
    voice,
    F.voice,
    StateFilter(PostState.message)
)
router.message.register(
    document,
    F.document,
    StateFilter(PostState.message)
)
router.message.register(
    sticker,
    F.sticker,
    StateFilter(PostState.message)
)
router.message.register(
    poll,
    F.poll,
    StateFilter(PostState.message)
)
router.message.register(
    album,
    F.media_group_id,
    StateFilter(PostState.message)
)
