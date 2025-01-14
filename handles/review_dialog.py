from aiogram import Router, types,F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup

review_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    contact = State()
    rate = State()
    extra_comments = State()


user_reviews = set()


@review_router.callback_query(F.data=="review")
async def start_review(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id in user_reviews:
        await callback.message.answer("Вы уже оставляли отзыв. Спасибо!")
        await state.clear()
    else:
        await callback.message.answer("Как вас зовут?")
        await state.set_state(RestaurantReview.name)


@review_router.message(RestaurantReview.name)
async def handle_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Пожалуйста, укажите ваш номер телефона или имя пользователя в Instagram:")
    await state.set_state(RestaurantReview.contact)


@review_router.message(RestaurantReview.contact)
async def handle_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer("Поставьте нам оценку от 1 до 5:")
    await state.set_state(RestaurantReview.rate)


@review_router.message(RestaurantReview.rate)
async def handle_rate(message: types.Message, state: FSMContext):
    if message.text.isdigit() and 1 <= int(message.text) <= 5:
        await state.update_data(rate=message.text)
        await message.answer("Есть ли у вас дополнительные комментарии или жалобы? (если нет, просто напишите \"нет\")")
        await state.set_state(RestaurantReview.extra_comments)
    else:
        await message.answer("Пожалуйста, укажите число от 1 до 5.")


@review_router.message(RestaurantReview.extra_comments)
async def handle_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()

    review_text = (
        f"Спасибо за ваш отзыв!\n"
        f"Имя: {data['name']}\n"
        f"Контакт: {data['contact']}\n"
        f"Оценка: {data['rate']}\n"
        f"Комментарии: {data['extra_comments']}"
    )

    await message.answer(review_text)

    user_reviews.add(message.from_user.id)

    await state.clear()
