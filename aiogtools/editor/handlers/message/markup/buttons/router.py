from aiogram import Router
from aiogram.filters import StateFilter

# Handlers
from .get_name import get_name
from .get_url import get_url

# States
from .....states import PostState


router = Router()

router.message.register(
    get_name,
    StateFilter(PostState)
)
router.message.register(
    get_url,
    StateFilter(PostState)
)
