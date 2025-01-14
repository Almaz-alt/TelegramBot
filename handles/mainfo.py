from aiogram import Router, types
from aiogram.filters import Command


myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def myinfo_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username if message.from_user.username else "не указано"

    logger.info(f"User {first_name} ({user_id}) requested info.")
    await message.answer(
        f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш ник: {username}"
    )
