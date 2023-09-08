from aiogram import Router, F

# Handlers
from .edit import edit_media
from .delete import delete_media

# Callback data
from ....cbdata import MediaCallbackData

router = Router()

router.callback_query.register(
    edit_media,
    MediaCallbackData.filter(F.action == 'edit')
)
router.callback_query.register(
    delete_media,
    MediaCallbackData.filter(F.action == 'delete')
)
