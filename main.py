# # from application import app, api
# # from Controllers.itemConroller import ItemController
# # from Controllers.pageController import PageConroller
# #
# # if __name__ == "__main__":
# #     api.add_resource(ItemController)
# #     api.add_resource(PageConroller)
# #
# #     app.run(debug=True, port=3000, host='127.0.0.1')
#
# import logging
# import asyncio
# import sys
# from asyncio import run_coroutine_threadsafe
#
# from aiogram import Bot, Dispatcher
# from Tarkov_Market_bot.webApp.config import TOKEN_BOT
# from aiogram.enums import ParseMode
# from aiohttp import web
# from aiohttp_wsgi import WSGIHandler
#
from Tarkov_Market_bot.handlers.handlers import router
#
# from application import app, api
# from Controllers.itemConroller import ItemController
# from Controllers.pageController import PageConroller
#
#
# async def start_bot_separate_loop():
#     print("start_bot_separate_loop - active")
#     loop = asyncio.new_event_loop()
#     print(f"Loop: {loop}")
#     asyncio.set_event_loop(loop)
#     bot = Bot(token=TOKEN_BOT, parse_mode=ParseMode.HTML)
#     dp = Dispatcher()
#     dp.include_router(router)
#     await dp.start_polling(bot)
#
# @web.middleware
# async def wsgi_middleware(request, handler):
#     def start_response(status, headers):
#         response = web.Response(status=status, headers=headers)
#         return response.prepare(request)
#
#     environ = {
#         'wsgi.version': (1, 0),
#         'wsgi.url_scheme': request.scheme,
#         'wsgi.input': await request.read(),
#         'wsgi.errors': sys.stderr,
#         'wsgi.multithread': False,
#         'wsgi.multiprocess': False,
#         'wsgi.run_once': False
#     }
#
#     response = await handler(environ, start_response)
#     return response
#
# async def on_startup(app):
#     wsgi_handler = WSGIHandler(app)
#     asyncio.create_task(start_bot_separate_loop())
#     print("Задача для бота создана")
#
# async def main():
#     api.add_resource(ItemController)
#     api.add_resource(PageConroller)
#     logging.basicConfig(level=logging.INFO)
#     run_coroutine_threadsafe(app.run(host='127.0.0.1', port=3001), asyncio.get_event_loop())
#
#     # app = web.Application()
#     # app.on_startup.append(on_startup)
#     # web.run_app(app, host='127.0.0.1', port=3001)
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
#


import logging
import asyncio
import sys
from asyncio import run_coroutine_threadsafe
from multiprocessing import Process

from aiogram import Bot, Dispatcher
from Tarkov_Market_bot.webApp.config import TOKEN_BOT
from aiogram.enums import ParseMode

from application import app, api
from Controllers.itemConroller import ItemController
from Controllers.pageController import PageConroller


async def start_bot():
    print("Это дерьмо заводится...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    bot = Bot(token=TOKEN_BOT, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)

def run_bot():
    asyncio.run(start_bot())

def run_flask():
    api.add_resource(ItemController)
    api.add_resource(PageConroller)
    app.run(host='127.0.0.1', port=3001)

if __name__ == "__main__":
    botProcess = Process(target=run_bot)
    flaskProcess = Process(target=run_flask)

    botProcess.start()
    flaskProcess.start()

    botProcess.join()
    flaskProcess.join()