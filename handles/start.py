from aiogram import Router, types
from aiogram.filters import Command

from handles.review_dialog import review_router

start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='review',callback_data='review')],
    ])
    await message.answer(f"Привет, {user_name}! Мои команды:\n"
                         f"/myinfo\n"
                         f"/random\n"
                         f"/recipe",reply_markup=keyboard)

