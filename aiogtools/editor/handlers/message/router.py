from aiogram import Router, F
from aiogram.filters import StateFilter

# Handlers
from .text import text
from .parse_media import parse_media
from .sticker import sticker
from .poll import poll
from .album import get_album
from .replace_links import replace_links

# States
from ...states import PostState


router = Router()

router.message.register(
    text,
    F.text,
    StateFilter(PostState.message, PostState.edit_text)
)
router.message.register(
    parse_media,
    ~F.media_group_id,
    StateFilter(PostState.message, PostState.edit_media, PostState.edit)
)
router.message.register(
    get_album,
    F.media_group_id,
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
    replace_links,
    F.text,
    StateFilter(PostState.replace_links)
)
