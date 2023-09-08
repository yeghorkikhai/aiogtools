from aiogram import Router, F

# Handlers
from .panel import panel
from .replace_links import replace_links

# Callback data
from ...cbdata import BaseCallbackData

# Routers
from .text.router import router as text_router
from .media.router import router as media_router
from .markup.router import router as markup_router
from .switches.router import router as switches_router

router = Router()

router.include_router(text_router)
router.include_router(media_router)
router.include_router(markup_router)
router.include_router(switches_router)

router.callback_query.register(
    panel,
    BaseCallbackData.filter(F.action == 'panel')
)
router.callback_query.register(
    replace_links,
    BaseCallbackData.filter(F.action == 'replace_links')
)
