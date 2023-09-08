from aiogram import Router


class Calendar:
    router: Router = Router()

    def __init__(self):
        self.__prepare()

    def __prepare(self):
        pass
        
    def export_router(self):
        return self.router
