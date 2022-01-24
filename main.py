import logging
import os

from aiogram import Bot, Dispatcher, executor

API_TOKEN = os.environ.get("token")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, skip_updates=True)
