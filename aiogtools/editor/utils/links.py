from aiogram.types import MessageEntity


def replace_all_links(
        text: str | None,
        entities: list[MessageEntity] | None,
        markup: str | None,
        link: str
):
    pass


def find_by_name_and_replace(
        text: str,
        entities: list[MessageEntity] | None,
        links: list[set[str, str]]
):
    pass
