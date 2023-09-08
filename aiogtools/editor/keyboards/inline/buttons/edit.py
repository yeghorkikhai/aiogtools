from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ....cbdata import ButtonCallbackData


def edit_button_keyboard(
        col: int,
        row: int
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='‹‹ Назад',
            callback_data=ButtonCallbackData(
                action='self',
                col=col,
                row=row
            ).pack()
        )
    )
    return InlineKeyboardMarkup(
        inline_keyboard=builder.export()
    )
