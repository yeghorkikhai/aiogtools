from aiogram import Router

from .message.router import router as message_router
from .callback_query.router import router as callback_query_router

router = Router()

router.include_router(message_router)
router.include_router(callback_query_router)
