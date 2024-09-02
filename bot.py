import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TELEGRAM_API_TOKEN, WEATHER_API_KEY

logging.basicConfig(level=logging.INFO)

# Функция для получения погоды
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

# Инициализация диспетчера
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Привет! Введите название города, чтобы получить прогноз погоды.")

@dp.message()
async def send_weather(message: Message):
    city = message.text.strip()
    weather_info = get_weather(city)
    await message.answer(weather_info, parse_mode=ParseMode.HTML)

async def main():
    bot = Bot(token=TELEGRAM_API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())