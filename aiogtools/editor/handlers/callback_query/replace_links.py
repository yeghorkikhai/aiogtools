from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ...states import PostState
from ...keyboards.inline import replace_links_keyboard


async def replace_links(
        callback_query: CallbackQuery,
        state: FSMContext
):
    await state.set_state(PostState.replace_links)

    await callback_query.message.edit_text(
        text='замена ссылок',
        reply_markup=replace_links_keyboard()
    )
