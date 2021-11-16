import asyncio
import datetime
import calendar
import logging

from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
datetime_now = datetime.datetime.now
first_weekday_this_month = (datetime_now() - datetime.timedelta(days=datetime_now().day-1)).isoweekday
length_month = calendar.monthlen(datetime_now().year, datetime_now().month)
today_weekday = datetime_now().isoweekday


def get_keyboard():
    buttons_last_month = [types.InlineKeyboardButton(text=" ", callback_data="pass") for i in range(1,first_weekday_this_month())]
    buttons = [
        types.InlineKeyboardButton(text="1", callback_data="num_decr"),
        types.InlineKeyboardButton(text="2", callback_data="num_incr"),
        types.InlineKeyboardButton(text="3", callback_data="num_finish")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=7)
    keyboard.add(*buttons_last_month,*buttons)
    return keyboard

@dp.message_handler(commands="calendar")
async def cmd_numbers(message: types.Message):
    await message.answer("Calendar", reply_markup=get_keyboard())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)