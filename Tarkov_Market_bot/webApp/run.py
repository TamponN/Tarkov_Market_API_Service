import logging
import asyncio

from aiogram import Bot, Dispatcher
from Tarkov_Market_bot.webApp.config import TOKEN_BOT
from aiogram.enums import ParseMode

from Tarkov_Market_bot.handlers.handlers import router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=TOKEN_BOT,parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped manually')

