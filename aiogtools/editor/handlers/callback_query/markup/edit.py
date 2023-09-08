from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....keyboards.inline import edit_markup_keyboard


async def edit_markup(
        callback_query: CallbackQuery,
        state: FSMContext,
        bot: Bot
):
    state_data = await state.get_data()

    markup = state_data.get('markup')

    await callback_query.message.edit_text(
        text='a',
        reply_markup=edit_markup_keyboard(
            has_markup=bool(markup),
            markup=markup
        )
    )
