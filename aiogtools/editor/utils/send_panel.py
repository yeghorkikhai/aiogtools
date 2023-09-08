from aiogram import Bot
from aiogram.fsm.context import FSMContext

from ..keyboards.inline import panel_keyboard


async def send_panel(
        chat_id: int,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()

    message = await bot.send_message(
        chat_id=chat_id,
        text="Текст",
        reply_markup=panel_keyboard(
            is_album=False,
            has_markup=bool(state_data.get("markup")),
            has_media=not (state_data.get("text")),
            media_position=state_data.get("media_position"),
            has_text=bool(state_data.get("text")) or bool(state_data.get("caption")),
            has_spoiler=state_data.get("has_spoiler"),
            disable_web_page_preview=state_data.get("disable_web_page_preview"),
            disable_notifications=state_data.get("disable_notifications"),
            back_title=state_data.get("back_title"),
            back_callback_data=state_data.get("back_callback_data"),
            then_title=state_data.get("then_title"),
            then_callback_data=state_data.get("then_callback_data"),
            allowed_methods=state_data.get('allowed_methods')
        )
    )

    await state.update_data({
        "editor_message_id": message.message_id
    })
