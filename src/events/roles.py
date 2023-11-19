import discord
from discord import RawReactionActionEvent
from loguru import logger

from src.main import bot
from src.utils.constants import roles_ids


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
