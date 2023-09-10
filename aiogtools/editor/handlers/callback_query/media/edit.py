from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....cbdata import MediaCallbackData
from ....keyboards.inline import edit_media_keyboard
from ....states import PostState
from ....utils.media import switch_media_position
from ....utils.refresh import refresh


async def edit_media(
        callback_query: CallbackQuery,
        callback_data: MediaCallbackData,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()
    has_media = state_data.get('text') is None or state_data.get("media_position")
    has_text = bool(state_data.get("text")) or bool(state_data.get("caption"))

    if state_data.get("media_position") != callback_data.position:
        is_switch = await switch_media_position(
            state=state,
            bot=bot,
            media_position=callback_data.position
        )
    else:
        is_switch = None

    await state.update_data({
        "media_position": callback_data.position
    })

    await state.set_state(PostState.edit_media)

    if is_switch:
        chat_id = callback_query.message.chat.id
        await refresh(chat_id, state, bot)
        return

    await callback_query.message.edit_text(
        text='sd',
        reply_markup=edit_media_keyboard(
            has_media=has_media,
            has_text=has_text,
            position=callback_data.position
        )
    )
