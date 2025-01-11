from dotenv import dotenv_values
from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.filters import Command
import random
import logging


token = dotenv_values('.env')['TOKEN']
bot = Bot(token=token)
dp = Dispatcher()


names = ['name', 'bektur', 'igor']

@dp.message(Command('my_info'))
async def my_info(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}')

@dp.message(Command('random'))
async def random_name(message: types.Message):
    random_name = random.choice(names)
    await message.answer(random_name)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    run(main())
