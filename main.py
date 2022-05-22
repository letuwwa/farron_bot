from aiogram import executor
from bot.config import dp


try:
    from bot.handlers import *
except ImportError:
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
