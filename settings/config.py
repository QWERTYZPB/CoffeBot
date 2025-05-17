from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from environs import Env

import os

os.environ.clear()

env = Env()
env.read_env()
# print(env.path())
# admins=env('ADMIN_IDS')
# print('admins:', admins)
ADMIN_IDS: list[int] = list(map(int, env('ADMIN_IDS').split(',')))

BOT_TOKEN = env('BOT_TOKEN')
SUPPORT_USERNAME = env('SUPPORT_USERNAME')

bot=Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='html'))
dp=Dispatcher()
