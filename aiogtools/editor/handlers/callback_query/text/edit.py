from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....keyboards.inline import edit_text_keyboard
from ....states import PostState


async def edit_text(
        callback_query: CallbackQuery,
        state: FSMContext
):
    state_data = await state.get_data()

    await state.set_state(PostState.edit_text)

    has_text = bool(state_data.get("text")) or bool(state_data.get("caption"))
    has_media = not (state_data.get("text")) or state_data.get("media_url")

    await callback_query.message.edit_text(
        text='d',
        reply_markup=edit_text_keyboard(
            has_text=has_text,
            has_media=has_media
        )
    )
