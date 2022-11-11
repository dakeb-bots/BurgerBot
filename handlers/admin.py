from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot

import messages as msg
from config import ADMIN_ID

class Admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Start dialog
async def start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await Admin.photo.set()
        await bot.send_message(message.chat.id, 'Upload a photo of the dish')
    else:
        await bot.send_message(message.chat.id, 'You do not have access to this command 🔒')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await Admin.next()
    await bot.send_message(message.chat.id, 'Enter the name')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Admin.next()
    await bot.send_message(message.chat.id, 'Enter description')

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await Admin.next()
    await bot.send_message(message.chat.id, 'Enter price')

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    async with state.proxy() as data:
        await bot.send_message(message.chat.id, f'Название: {str(data)}')
    # Clear all data!
    await state.finish()

async def cancel_state(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is None:
        return
    await state.finish()
    await bot.send_message(message.chat.id, 'Canceled')
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start, commands=['upload'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=Admin.photo)
    dp.register_message_handler(load_name, state=Admin.name)
    dp.register_message_handler(load_description, state=Admin.description)
    dp.register_message_handler(load_price, state=Admin.price)

    dp.register_message_handler(cancel_state, state='*', commands=['cancel'])