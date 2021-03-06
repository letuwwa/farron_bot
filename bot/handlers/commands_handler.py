from aiogram import types
from bot.config import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['user'])
async def send_user(message: types.Message):
    await message.reply(f"{message.from_user.username}, {message.from_user.id}, {message.get_command()}")
