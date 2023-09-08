from aiogram import Router, F

# Handlers
from .disable_web_page_preview_switch import disable_web_page_preview_switch
from .disable_notifications_switch import disable_notifications_switch
from .media_spoiler_switch import media_spoiler_switch

# Callback data
from ....cbdata import BaseCallbackData

router = Router()

router.callback_query.register(
    disable_web_page_preview_switch,
    BaseCallbackData.filter(F.action == 'disable_web_page_preview_switch')
)
router.callback_query.register(
    disable_notifications_switch,
    BaseCallbackData.filter(F.action == 'disable_notifications_switch')
)
router.callback_query.register(
    media_spoiler_switch,
    BaseCallbackData.filter(F.action == 'media_spoiler_switch')
)
