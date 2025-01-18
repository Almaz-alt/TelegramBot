from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    user_name = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='review', callback_data='review')],
    ])
    await message.answer(f"Привет, {user_name}! Мои команды:\n"
                         f"/myinfo\n"
                         f"/random\n"
                         f"/recipe", reply_markup=keyboard)


from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


class Review(StatesGroup):
    start = State()
    rating = State()
    comment = State()
    date = State()


rating_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='rating:1'),
            InlineKeyboardButton(text='2', callback_data='rating:2'),
            InlineKeyboardButton(text='3', callback_data='rating:3'),
            InlineKeyboardButton(text='4', callback_data='rating:4'),
            InlineKeyboardButton(text='5', callback_data='rating:5'),
        ]
    ]
)


async def save_review_to_db(state: FSMContext):
    data = await state.get_data()
    print(f"Сохранено в БД: {data}")

    # db.execute("INSERT INTO reviews (rating, comment, date) VALUES (?, ?, ?)",
    #            (data["rating"], data["comment"], data.get("date")))


if __name__ == "__main__":
    from aiogram import Bot, Dispatcher
    from aiogram.fsm.storage.memory import MemoryStorage
    import asyncio

    TOKEN = "TOKEN"
    bot = Bot(token=token)
    dp = Dispatcher()

    register_handlers(router)


    async def main():
        await dp.start_polling(bot)


    asyncio.run(main())
