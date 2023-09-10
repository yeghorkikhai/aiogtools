from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ...enums import MediaPosition
from ...cbdata import (
    BaseCallbackData,
    MediaCallbackData
)


def edit_media_keyboard(
        has_media: bool,
        has_text: bool,
        position: MediaPosition
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f"{'🔸' if position == MediaPosition.UP else ''} Над",
            callback_data=MediaCallbackData(
                action='edit',
                position=MediaPosition.UP
            ).pack()
        ),
        InlineKeyboardButton(
            text=f"{'🔸' if position == MediaPosition.DOWN else ''} Під",
            callback_data=MediaCallbackData(
                action='edit',
                position=MediaPosition.DOWN
            ).pack()
        )
    )
    if has_media and has_text:
        builder.row(
            InlineKeyboardButton(
                text=f"Видалити медіа",
                callback_data=MediaCallbackData(
                    action='delete',
                    position=position
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
