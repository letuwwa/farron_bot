import logging
import os

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.environ.get("token")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['user'])
async def send_user(message: types.Message):
    await message.reply(f"{message.from_user.username}, {message.from_user.id}, {message.text}")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
