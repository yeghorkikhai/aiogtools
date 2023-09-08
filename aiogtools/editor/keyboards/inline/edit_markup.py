from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ...cbdata import (
    BaseCallbackData,
    ButtonCallbackData
)


def edit_markup_keyboard(
        markup: list[list[InlineKeyboardButton]],
        has_markup: bool
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    if has_markup:
        builder.row(
            *[
                [
                    InlineKeyboardButton(
                        text=button.text,
                        callback_data=ButtonCallbackData(
                            action='self',
                            col=col,
                            row=row
                        ).pack()
                    ) for col, button in enumerate(buttons)
                ] for row, buttons in enumerate(markup)
            ]
        )
        builder.row(
            InlineKeyboardButton(
                text="Видалити кнопки",
                callback_data=BaseCallbackData(
                    action='delete_markup'
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
