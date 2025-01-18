from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup

router = Router()


class Review(StatesGroup):
    name = State()
    contact = State()
    rate = State()
    comment = State()
    date = State()


rating_kb = InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='1', callback_data='rate:1'),
     types.InlineKeyboardButton(text='2', callback_data='rate:2'),
     types.InlineKeyboardButton(text='3', callback_data='rate:3'),
     types.InlineKeyboardButton(text='4', callback_data='rate:4'),
     types.InlineKeyboardButton(text='5', callback_data='rate:5'), ],
])


@router.callback_query(F.data == 'review')
async def start_review(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Оцените ваш опыт от 1 до 5:", reply_markup=rating_kb)
    await state.set_state(Review.rate)


@router.callback_query(Review.rate)
async def rating_chosen(callback: types.CallbackQuery, state: FSMContext):
    rating = int(callback.data.split(":")[1])
    await state.update_data(rating=rating)
    await callback.message.edit_text(f"Вы выбрали оценку: {rating}\nНапишите ваш комментарий:")
    await state.set_state(Review.comment)


@router.message(Review.comment)
async def comment_received(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await message.answer("Укажите дату посещения (например, 2023-12-31)")
    await state.set_state(Review.date)


@router.message(Review.date)
async def date_received(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer("Спасибо за ваш отзыв!")
    await state.clear()
