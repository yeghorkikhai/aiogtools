from aiogram import Router, F

# Handlers
from .edit import edit_markup
from .delete import delete_markup

# Callback data
from ....cbdata import BaseCallbackData

# Routers
from .buttons.router import router as buttons_router


router = Router()

router.include_router(buttons_router)

router.callback_query.register(
    edit_markup,
    BaseCallbackData.filter(F.action == 'edit_markup')
)
router.callback_query.register(
    delete_markup,
    BaseCallbackData.filter(F.action == 'delete_markup')
)
