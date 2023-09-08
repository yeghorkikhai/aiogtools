from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....cbdata import MediaCallbackData
from ....keyboards.inline import edit_media_keyboard
from ....states import PostState


async def edit_media(
        callback_query: CallbackQuery,
        callback_data: MediaCallbackData,
        state: FSMContext
):
    state_data = await state.get_data()
    has_media = state_data.get('text') is None

    await state.update_data({
        "media_position": callback_data.position
    })
    await state.set_state(PostState.edit_media)

    await callback_query.message.edit_text(
        text='sd',
        reply_markup=edit_media_keyboard(
            has_media=has_media,
            position=callback_data.position
        )
    )
