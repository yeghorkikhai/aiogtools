from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ...cbdata import (
    BaseCallbackData,
    MediaCallbackData
)
from ...enums import (
    MediaPosition,
    AllowedMethods
)


def panel_keyboard(
        is_album: bool,
        has_text: bool,
        has_media: bool,
        media_position: MediaPosition,
        has_markup: bool,
        has_spoiler: bool,
        disable_web_page_preview: bool,
        disable_notifications: bool,
        back_callback_data: str,
        then_callback_data: str,
        back_title: str,
        then_title: str,
        allowed_methods: list[AllowedMethods] | None
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=f"{'Додати' if not has_text else 'Редагувати' } текст",
            callback_data=BaseCallbackData(
                action='edit_text'
            ).pack()
        ),
        InlineKeyboardButton(
            text=f"{'Додати' if not has_media else 'Редагувати'} медіа",
            callback_data=MediaCallbackData(
                action='edit',
                position=media_position
            ).pack()
        )
    )
    if not is_album:
        builder.row(
            InlineKeyboardButton(
                text=f"{'Додати' if not has_markup else 'Редагувати'} URL-Кнопки",
                callback_data=BaseCallbackData(
                    action='edit_markup'
                ).pack()
            )
        )
    if allowed_methods is None or AllowedMethods.REPLACE_LINKS in allowed_methods:
        builder.row(
            InlineKeyboardButton(
                text="Замінити посилання",
                callback_data=BaseCallbackData(
                    action="replace_links"
                ).pack()
            )
        )
    row = []
    if allowed_methods is None or AllowedMethods.DISABLE_NOTIFICATIONS_SWITCH in allowed_methods:
        row.append(
            InlineKeyboardButton(
                text='🔔' if not disable_notifications else '🔕',
                callback_data=BaseCallbackData(
                    action='disable_notifications_switch'
                ).pack()
            )
        )
    if allowed_methods is None or AllowedMethods.DISABLE_WEB_PAGE_PREVIEW_SWITCH in allowed_methods:
        row.append(
            InlineKeyboardButton(
                text=f"Превью {'☑️' if not disable_web_page_preview else '✅'}",
                callback_data=BaseCallbackData(
                    action='disable_web_page_preview_switch'
                ).pack()
            )
        )
    builder.row(*row)

    if allowed_methods is None or AllowedMethods.SPOILER_SWITCH in allowed_methods:
        builder.row(
            InlineKeyboardButton(
                text=f"Спойлер {'✅' if not has_spoiler else '☑️'}",
                callback_data=BaseCallbackData(
                    action='media_spoiler_switch'
                ).pack()
            )
        )
    builder.row(
        InlineKeyboardButton(
            text=back_title if back_title is not None else "‹‹ Назад",
            callback_data=back_callback_data
        ),
        InlineKeyboardButton(
            text=then_title if then_title is not None else "Вперед ››",
            callback_data=then_callback_data
        )
    )
    return InlineKeyboardMarkup(
        inline_keyboard=builder.export()
    )
