from discord import FFmpegPCMAudio, Intents
from discord.ext import commands
from yt_dlp import YoutubeDL

from src import config


bot = commands.Bot(command_prefix='!', intents=Intents.all())


@bot.command()
async def play(ctx, url: str):
    voice_channel = await ctx.message.author.voice.channel.connect()

    with YoutubeDL(config.YDL_OPTIONS) as ydl:
        if 'https://' in url:
            info = ydl.extract_info(url, download=False)
        else:
            info = ydl.extract_info(
                executable=f'ytseatch: {url}',
                download=False
            )['entries'][0]
    link = info['formats'][0]['url']

    voice_channel.play(
        FFmpegPCMAudio(
            executable=r'..\ffmpeg\ffmpeg.exe',
            source=link,
            **config.FFMPEG_OPTIONS
        )
    )


if __name__ == '__main__':
    bot.run(config.BOT_TOKEN)
