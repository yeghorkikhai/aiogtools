from aiogram import Router, F

# Handlers
from .self import self
from .edit_name import edit_name
from .edit_url import edit_url

# Callback data
from aiotools_editor.cbdata import ButtonCallbackData


router = Router()

router.callback_query.register(
    self,
    ButtonCallbackData.filter(F.action == 'self')
)
router.callback_query.register(
    edit_name,
    ButtonCallbackData.filter(F.action == 'edit_name')
)
router.callback_query.register(
    edit_url,
    ButtonCallbackData.filter(F.action == 'edit_url')
)
