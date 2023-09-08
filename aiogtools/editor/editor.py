from aiogram import Router

from .handlers.router import router as handlers_router
from .middlewares import AlbumMiddleware


class Editor:

    router: Router = Router()

    def __init__(self):
        self.__prepare()

    def __prepare(self):
        self.router.message.middleware(AlbumMiddleware())
        self.router.include_router(handlers_router)

    def export_router(self):
        return self.router
