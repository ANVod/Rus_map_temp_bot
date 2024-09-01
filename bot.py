import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TELEGRAM_API_TOKEN, WEATHER_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"Погода в городе {city}:\nТемпература: {temp}°C\nОписание: {description}"
    else:
        return "Не удалось получить данные о погоде. Проверьте название города."

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Введите название города, чтобы получить прогноз погоды.")

@dp.message_handler()
async def send_weather(message: types.Message):
    city = message.text.strip()
    weather_info = get_weather(city)
    await message.reply(weather_info, parse_mode=ParseMode.MARKDOWN_V2)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)