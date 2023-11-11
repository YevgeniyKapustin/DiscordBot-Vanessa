from discord import Message

from src import config


class Text(object):
    __slots__ = ('__message',)

    def __init__(self, message: Message):
        self.__message = message

    async def check(self) -> bool:
        message = self.__message
        if not message.author.bot and message.channel.id == config.CHANNEL_ID:
            return True
        return False
