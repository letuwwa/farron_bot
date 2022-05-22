import os
import logging
from aiogram import Bot, Dispatcher


TELEGRAM_TOKEN = os.environ.get("TOKEN")


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)
