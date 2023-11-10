"""Модуль для класса Settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Конфигурация бота."""
    BOT_TOKEN: str        # Токен от бота
    CHANNEL_ID: str       # ID канала, в котором бот работает

    class Config:
        """Настройка файла .env."""
        env_file = '../../.env'
        env_file_encoding = 'utf-8'
