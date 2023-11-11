"""Модуль для класса Settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Конфигурация бота."""
    BOT_TOKEN: str        # Токен от бота
    CHANNEL_ID: int       # ID канала, в котором бот работает

    YDL_OPTIONS: dict = {
        'format': 'worstaudio/best',
        'noplaylist': 'False',
        'simulate': 'True',
        'key': 'FFmpegExtractAudio'
    }
    FFMPEG_OPTIONS: dict = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }

    class Config:
        """Настройка файла .env."""
        env_file = '../../.env'
        env_file_encoding = 'utf-8'
