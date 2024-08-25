import logging
import asyncio
from aiogram import Bot, Dispatcher
from handlers import career_choice, common
import config

async def main():
    API_TOKEN = config.token

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    dp.include_router(career_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
