from aiogram import Router, F

# Handlers
from .edit import edit_text
from .delete import delete_text

# Callback data
from ....cbdata import BaseCallbackData

router = Router()

router.callback_query.register(
    edit_text,
    BaseCallbackData.filter(F.action == 'edit_text')
)
router.callback_query.register(
    delete_text,
    BaseCallbackData.filter(F.action == 'delete_text')
)
