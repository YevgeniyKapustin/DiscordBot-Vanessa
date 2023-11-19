from random import randint, choice

import discord
from discord import Intents, ApplicationContext, Option, RawReactionActionEvent
from discord.ext import commands
from loguru import logger

from src import config
from src.utils.constants import roles_ids

bot = commands.Bot(intents=Intents.all())


@bot.event
async def on_ready():
    logger.info('Бот запущен')


@bot.slash_command(description='Выбор случайной фракции в героях 3')
async def fraction_heroes_3(ctx: ApplicationContext):
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
    await ctx.respond(f'🎲 {choice(fractions)}')


@bot.slash_command(description='Выбор случайной фракции в героях 5')
async def fraction_heroes_5(ctx: ApplicationContext):
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
    await ctx.respond(f'🎲 {choice(fractions)}')


@bot.slash_command(description='Бросок кубика с определенным кол-вом сторон')
async def dice(
        ctx: ApplicationContext,
        sides: Option(int, description='Количество сторон кубика')
):
    await ctx.respond(f'🎲 {randint(1, sides)}')


@bot.event
async def on_raw_reaction_add(payload: RawReactionActionEvent):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.id == 1175767816977264741:
        for reaction in roles_ids:
            if payload.emoji.name == reaction:
                user = message.guild.get_member(payload.user_id)
                role = discord.utils.get(
                    message.guild.roles,
                    id=roles_ids.get(reaction)
                )
                if user and role:
                    await user.add_roles(role)
                    logger.info(
                        f'Добавлена роль "{role}" пользователю {user.name}'
                    )


@bot.event
async def on_raw_reaction_remove(payload: RawReactionActionEvent):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if message.id == 1175767816977264741:
        for reaction in roles_ids:
            if payload.emoji.name == reaction:
                role = discord.utils.get(
                    message.guild.roles,
                    id=roles_ids.get(reaction)
                )
                if member and role:
                    await member.remove_roles(role)
                    logger.info(
                        f'Удалена роль "{role}" у пользователя {member.name}'
                    )

if __name__ == '__main__':
    bot.run(config.BOT_TOKEN)
