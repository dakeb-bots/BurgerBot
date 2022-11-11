from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot

import messages as msg
from config import ADMIN_ID, ADMIN_LOGIN, ADMIN_PASSWORD

class Auth(StatesGroup):
    login = State()
    password = State()

async def login(message: types.Message):
    await Auth.login.set()
    await bot.send_message(message.chat.id, 'Enter login or /cancel')

async def load_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
    await Auth.next()
    await bot.send_message(message.chat.id, 'Enter password')

async def load_password(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text
        if data['login'] == ADMIN_LOGIN and data['password'] == ADMIN_PASSWORD:
            await bot.send_message(message.chat.id, 'Success!')
            ADMIN_ID.append(message.from_user.id)
            print(f'{message.from_user.username} owned')
        else:
            bot.send_message(message.chat.id, 'Error!')
    # Clear all data
    await state.finish()

async def cancel_state(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is None:
        return
    await state.finish()
    await bot.send_message(message.chat.id, 'Canceled')

def register_handlers_auth(dp: Dispatcher):
    dp.register_message_handler(login, commands=['admin'], state=None)
    dp.register_message_handler(load_login, state=Auth.login)
    dp.register_message_handler(load_password, state=Auth.password)

    dp.register_message_handler(cancel_state, state='*', commands=['cancel'])

