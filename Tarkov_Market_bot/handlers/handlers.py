from aiogram import Router, Bot
from aiogram.client import bot
from aiogram.types import Message, WebAppInfo, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
)

from Tarkov_Market_bot.webApp.config import TOKEN_BOT
import Tarkov_Market_bot.Keyboards.keyboards
from Tarkov_Market_bot.Keyboards.keyboards import *
from Controllers.itemConroller import (
    _apiService,
    _itemService
)

router = Router()

def get_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="Перейти", web_app=WebAppInfo(url = 'https://t.me/test_thiiiis_shit_bot'))
    return builder.as_markup()

""" кнопки: предметы, квесты """
main_builder = InlineKeyboardBuilder()

main_builder.row(
    InlineKeyboardButton(text="Предметы", callback_data="items"),
            InlineKeyboardButton(text="Квесты", callback_data="quests")
        )


@router.message(Command("Find"))
async def find_items(message: Message):
    # await message.reply("Что вам нужно?", reply_markup=Keyboards.keyboards.main_kb())
    await  message.answer("что вам нужно",reply_markup=Tarkov_Market_bot.Keyboards.keyboards.main_kb)


@router.message(CommandStart())
async def on_start(message: Message):
    username = message.from_user.first_name or message.from_user.username
    await message.answer("Привет, {username}! Как я могу помочь вам?".format(username=username),
                         reply_markup=get_kb())



@router.callback_query()
async def show_items_categories(query: CallbackQuery):
    if query.data == "items":
        await query.message.edit_reply_markup(reply_markup=Tarkov_Market_bot.Keyboards.keyboards.item_kb)


@router.callback_query()
async def go_bakc(query: CallbackQuery):
    if query == "back":
        await query.message.edit_reply_markup(reply_markup=Tarkov_Market_bot.Keyboards.keyboards.main_kb())


@router.message(Command("help"))
async def wait_help(message: Message):
    await message.answer('не ну вот так как-то')


"""Реализайция поиска через сообщения"""
bot = Bot(token=TOKEN_BOT)
@router.message()
async def get_message(message: Message):
    search_query = message.text
    items = _apiService.get_item_by_name(search_query)

    for item in items:
        name = item["name"]
        price = item["price"]
        avg24hPrice = item["avg24hPrice"]
        icon = item["icon"]

        await bot.send_photo(chat_id=message.chat.id, photo=icon,
                             caption=
                             f"Название: {name}\n"
                             f"Цена: {price}\n"
                             f"Средняя цена за 24 часа: {avg24hPrice}")



