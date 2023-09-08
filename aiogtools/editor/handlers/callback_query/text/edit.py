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

    has_text = True if (
            state_data.get('text') is not None or state_data.get('caption') is not None
    ) else False

    await callback_query.message.edit_text(
        text='d',
        reply_markup=edit_text_keyboard(
            has_text=has_text
        )
    )
