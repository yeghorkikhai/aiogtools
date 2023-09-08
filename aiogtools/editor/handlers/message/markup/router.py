from aiogram import Router
from aiogram.filters import StateFilter

# Handlers
from .get_url_buttons import get_url_buttons

# States
from ....states import PostState

# Routers
from .buttons.router import router as buttons_router

router = Router()

router.include_router(buttons_router)

router.message.register(
    get_url_buttons,
    StateFilter(PostState.edit_markup)
)
