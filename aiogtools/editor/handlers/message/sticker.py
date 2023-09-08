from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def sticker(
        message: Message,
        state: FSMContext
):
    await message.delete()

    await message.answer(
        text='Бот не працює зі стікерами надішліть пост'
    )
