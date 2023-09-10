import secrets

from aiogram import Bot
from aiohttp import (
    ClientSession,
    FormData
)


class Telegraph:
    bot: Bot
    api_url: str = "https://telegra.ph/upload"

    def __init__(self, bot: Bot):
        self.bot = bot

    async def __get_file_url(self, file_id: str) -> str:
        file_path = await self.__get_file_path(file_id=file_id)

        return f"https://api.telegram.org/file/bot{self.bot.token}/{file_path}"

    async def __get_file_path(self, file_id: str) -> str:
        file = await self.bot.get_file(file_id=file_id)
        return file.file_path

    async def __download_file(
            self,
            file_url: str
    ):
        pass

    async def upload_file_from_telegram(
            self,
            file_id: str,
            filename=None
    ) -> str:
        form = FormData(quote_fields=False)

        file_url = await self.__get_file_url(file_id=file_id)

        if filename is None:
            filename = 'filename'

        async with ClientSession() as session:
            async with session.get(file_url) as response:
                form.add_field(
                    secrets.token_urlsafe(8),
                    response.content,
                    filename=filename
                )
                async with session.post(self.api_url, data=form) as r:
                    result = await r.json()
                    return f"https://telegra.ph{result[0]['src']}"
