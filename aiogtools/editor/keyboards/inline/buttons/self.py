from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ....cbdata import (
    BaseCallbackData,
    ButtonCallbackData
)


def self_button_keyboard(
        col: int,
        row: int
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text='Змінити назву',
            callback_data=ButtonCallbackData(
                action='edit_name',
                col=col,
                row=row
            ).pack()
        ),
        InlineKeyboardButton(
            text='Змінити посилання',
            callback_data=ButtonCallbackData(
                action='edit_url',
                col=col,
                row=row
            ).pack()
        ),
        width=1
    )
    builder.row(
        InlineKeyboardButton(
            text='‹‹ Назад',
            callback_data=BaseCallbackData(
                action='edit_markup'
            ).pack()
        )
    )
    return InlineKeyboardMarkup(
        inline_keyboard=builder.export()
    )
