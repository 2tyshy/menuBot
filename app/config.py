from dataclasses import dataclass
from dotenv import load_dotenv
import os

@dataclass
class Settings:
    BOT_TOKEN: str

def load_settings() -> Settings:
    load_dotenv()
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        raise ValueError("BOT_TOKEN пуст. Укажите токен бота в .env (см. .env.example)")
    return Settings(BOT_TOKEN=token)
