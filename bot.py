from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import messages as msg

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Commands
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.full_name}! 🤖\nYou can ask me about the schedule or menu, a list of all the commands : /help')

@dp.message_handler(commands=['help'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, '/schedule — Schedule of work\n/menu — Delicious burger menu\n/address — Addresses of our burger joints')

@dp.message_handler(commands=['menu'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, msg.oops)

@dp.message_handler(commands=['schedule'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, 'Schedule 🕓\nMo-Fr: 09:00-20:00am\nSa-Su: 10:00-19:00am')

@dp.message_handler(commands=['address'])
async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, msg.oops)

# @dp.message_handler()
# async def echo(message: types.Message):
#    await bot.send_message(message.chat.id, message.text)

executor.start_polling(dp, skip_updates=True)