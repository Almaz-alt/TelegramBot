#
#
# import random
# from aiogram import Router, types
# from aiogram.filters import Command
#
# random_recipe = Router()
#
#
# @random_recipe.message(Command("recipe"))
# async def random_recipe_command(message: types.Message):
#     recipe_name, recipe = random.choice(list(recipes.items()))
#     logger.info(f"User {message.from_user.first_name} requested a random recipe: {recipe_name}.")
#     photo_path = recipe["photo"]
#     caption = recipe["caption"]
#
#     if os.path.exists(photo_path):
#         await message.answer_photo(photo=open(photo_path, 'rb'), caption=caption)
#     else:
#         await message.answer("Извините, изображение недоступно.")
#
#
#
#
#
# recipes = {
#     "salad": {
#         "photo": "images/salad.jpg",
#         "caption": "Рецепт салата: Огурцы, помидоры, листья салата, заправка из оливкового масла."
#     },
#     "soup": {
#         "photo": "images/soup.jpg",
#         "caption": "Рецепт борща: Свекла, капуста, картофель, морковь, мясо."
#     },
#     "pasta": {
#         "photo": "images/pasta.jpg",
#         "caption": "Рецепт пасты: Макароны, томатный соус, сыр, базилик."
#     }
# }
