import random
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv, dotenv_values
from aiogram.filters import Command
from asyncio import run


load_dotenv()
token = dotenv_values(".env")["TOKEN"]


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=token)
dp = Dispatcher(bot)

names = ['dfd', 'dfdf', 'dfdfd']


@dp.message(Command('start'))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    logger.info(f"User {user_name} started the bot.")  # Логирование старта пользователя
    await message.answer(f"Привет, {user_name}! Мои команды:\n"
                         f"/myinfo\n"
                         f"/random")


@dp.message(Command('myinfo'))
async def myinfo_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username if message.from_user.username else "не указано"

    logger.info(f"User {first_name} ({user_id}) requested info.")  # Логирование запроса информации
    await message.answer(
        f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш ник: {username}"
    )


@dp.message(Command('random'))
async def random_command(message: types.Message):
    random_name = random.choice(names)
    logger.info(f"User {message.from_user.first_name} requested a random name.")  # Логирование запроса случайного имени
    await message.answer(f"Случайное имя: {random_name}")


async def main():
    logger.info("Bot is starting...")  # Логирование старта бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())

