from aiogram import types, Dispatcher
from create_bot import bot, dp

import messages as msg

async def welcome(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello {message.from_user.full_name}! 🤖\nYou can ask me about the schedule or menu, a list of all the commands : /help')

async def help(message: types.Message):
    await bot.send_message(message.chat.id, '/schedule — Schedule of work\n/menu — Delicious burger menu\n/address — Addresses of our burger joints')

async def menu(message: types.Message):
    await bot.send_message(message.chat.id, msg.oops)

async def schedule(message: types.Message):
    await bot.send_message(message.chat.id, 'Schedule 🕓\nMo-Fr: 09:00-20:00am\nSa-Su: 10:00-19:00am')

async def address(message: types.Message):
    await bot.send_message(message.chat.id, msg.oops)

async def my_id(message: types.Message):
    await bot.send_message(message.chat.id, message.from_user.id)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(menu, commands=['menu'])
    dp.register_message_handler(schedule, commands=['schedule'])
    dp.register_message_handler(address, commands=['address'])
    dp.register_message_handler(my_id, commands=['id'])