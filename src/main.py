from discord import Bot, Intents, Message

from src import config

bot = Bot(intents=Intents.all())


@bot.event
async def echo(message: Message):
    if message.channel.id == config.CHANNEL_ID:
        await message.reply(message.content)

bot.run(config.BOT_TOKEN)
