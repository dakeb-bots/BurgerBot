from aiogram.utils import executor
from create_bot import dp

from handlers import client, admin, other, authorization
from config import ADMIN_ID

async def on_startup(_):
    print('I am alive!')
    print(f'admins: {ADMIN_ID}')

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
authorization.register_handlers_auth(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)