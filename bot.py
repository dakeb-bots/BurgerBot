from aiogram.utils import executor
from create_bot import dp

from handlers import client, admin, other

async def on_startup(_):
    print('I am alive!')

client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)