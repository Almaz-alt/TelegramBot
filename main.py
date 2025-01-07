import random
from aiogram import Bot, Dispatcher, types

from dotenv import load_dotenv, dotenv_values
from aiogram.filters import  Command
from asyncio import run
token = dotenv_values(".env")["TOKEN"]


bot = Bot(token=token)
dp = Dispatcher()


names = ['dfd','dfdf','dfdfd']

@dp.message(Command('start'))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"Привет, {user_name}Мои команды:\n"
                        f"/myinfo\n"
                         f"/random")



@dp.message(Command('myinfo'))
async def myinfo_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username if message.from_user.username else "не указано"

    await message.answer(
        f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш ник: {username}"
    )


# Обработчик команды /random
@dp.message(Command('random'))
async def random_command(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())

