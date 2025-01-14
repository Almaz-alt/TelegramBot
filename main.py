from asyncio import  run

import logging
from bot_config import bot, dp



from handles.start import start_router
from handles.mainfo import myinfo_router
# from handles.random import random_name_router
# from handles.random_recipe import random_recipe_router


async def main():

    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    # dp.include_router(random_name_router)
    # dp.include_router(random_recipe_router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)



if __name__ == "__main__":
    run(main())
