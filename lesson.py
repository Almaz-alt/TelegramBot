from aiogram.enums import ParseMode

import random
import logging
from aiogram import types, Bot, Dispatcher, executor
from aiogram.enums import ParseMode  # Исправленный импорт

API_TOKEN = 'YOUR_API_TOKEN_HERE'

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

recipes = {
    "салат": "Рецепт: Смешать овощи, приправить маслом.",
    "борщ": "Рецепт: Варить свеклу, добавить капусту и мясо."
}

async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в наш ресторан! Как мы можем помочь вам?")

async def menu_command(message: types.Message):
    await message.answer("Вот наше меню: 1. Салат 2. Борщ")

async def random_recipe_command(message: types.Message):
    dish = random.choice(list(recipes.keys()))
    caption = recipes[dish]
    await message.answer_photo(photo=f'images/{dish}.jpg', caption=caption)

dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(menu_command, commands=['menu'])
dp.register_message_handler(random_recipe_command, commands=['random_recipe'])

logging.basicConfig(level=logging.INFO)

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
