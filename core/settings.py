from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")


@dataclass
class Bot:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bot: Bot


def get_settings():
    return Settings(bot=Bot(bot_token=TOKEN, admin_id=int(ADMIN_ID)))


settings = get_settings()
