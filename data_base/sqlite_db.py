import sqlite3 as sql
from create_bot import bot

def sql_start():
    global base, cur
    base = sql.connect('burger.db')
    cur = base.cursor()
    if base:
        print('Database connected!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS admins(id TEXT PRIMARY KEY, username TEXT, login TEXT, password TEXT)')
    base.commit()

async def sql_add_command(state, table):
    async with state.proxy() as data:
        cur.execute(f'INSERT INTO {table} VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message, table):
    for ret in cur.execute(f'SELECT * FROM {table}').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n{ret[2]}\nPrice: {ret[-1]}$')