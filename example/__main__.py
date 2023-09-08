import asyncio

from aiogram import (
    Bot,
    Dispatcher,
    Router
)
from aiogram.enums import ParseMode

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from aiogram.types import (
    Message,
    BotCommand
)
from aiogram.filters import Command, CommandStart

from aiogtools.editor import Editor
from aiogtools.editor.utils.posts import create_post, edit_post

router = Router()


@router.message(CommandStart())
async def start_command(
        message: Message,
        state: FSMContext
):
    await create_post(
        state=state,
        back_callback_data="back",
        then_callback_data="next"
    )

    await message.answer(
        text="Надішли мені щось"
    )


@router.message(Command('/edit'))
async def edit_command(
        message: Message,
        state: FSMContext,
        bot: Bot
):
    pass


async def on_startup(bot: Bot):
    print("Start polling....")
    commands = [
        BotCommand(command='/start', description='Створити пост'),
        BotCommand(command='/edit', description='Редагувати пост')
    ]
    await bot.set_my_commands(commands=commands)


async def on_shutdown(bot: Bot):
    print("Shutting down....")


async def main():
    bot = Bot(token="6521287009:AAHgmASv9eI1pKttzAjYTnF6FhyV439xb1w", parse_mode=ParseMode.HTML)
    dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())

    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)

    dispatcher.include_router(router)

    editor = Editor()
    dispatcher.include_router(editor.export_router())

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
