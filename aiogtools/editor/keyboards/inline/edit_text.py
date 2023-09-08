from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ...cbdata import BaseCallbackData


def edit_text_keyboard(
        has_text: bool
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if has_text:
        builder.row(
            InlineKeyboardButton(
                text=f"Видалити текст",
                callback_data=BaseCallbackData(
                    action='delete_text'
                ).pack()
            )
        )
    builder.row(
        InlineKeyboardButton(
            text='‹‹ Назад',
            callback_data=BaseCallbackData(
                action='panel'
            ).pack()
        )
    )
    return InlineKeyboardMarkup(
        inline_keyboard=builder.export()
    )
