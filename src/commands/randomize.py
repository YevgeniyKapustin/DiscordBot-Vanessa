from random import choice, randint

from discord import ApplicationContext, Option, Cog


from src.main import bot


class GeneralCommands(Cog):
    def __init__(self, bot):
            self.bot = bot

    @cog_slash(
        description='Выбор случайной фракции в героях 3'
    )
    async def fraction_heroes_3(self: ApplicationContext):
        fractions = [
            'замок',
            'оплот',
            'башня',
            'инферно',
            'некрополис',
            'темница',
            'цитадель',
            'крепость',
            'причал',
        ]
        await self.respond(f'🎲 {choice(fractions)}')

    @bot.slash_command(
        description='Выбор случайной фракции в героях 5'
    )
    async def fraction_heroes_5(self: ApplicationContext):
        fractions = [
            'орден порядка',
            'инферно',
            'лесной союз',
            'некрополис',
            'лига теней',
            'академия волшебства',
            'подгорный народ',
            'великая орда'
        ]
        await self.respond(f'🎲 {choice(fractions)}')

    @bot.slash_command(
        description='Бросок кубика с определенным кол-вом сторон'
    )
    async def dice(
            self: ApplicationContext,
            sides: Option(int, description='Количество сторон кубика')
    ):
        await self.respond(f'🎲 {randint(1, sides)}')


def setup(bot):
    bot.add_cog(GeneralCommands(bot))
