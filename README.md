# Telegram Weather Bot

Этот проект представляет собой Telegram-бота, который предоставляет прогноз погоды для указанного пользователем города. Бот использует API OpenWeatherMap для получения данных о погоде.

## Установка

1. Склонируйте репозиторий или загрузите код проекта.

```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Перейдите в директорию проекта.

```bash
cd yourrepository
```

3. Создайте виртуальное окружение и активируйте его.

```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
```

4. Установите необходимые зависимости.

```bash
pip install -r requirements.txt
```

5. Создайте файл `config.py` в корне проекта и добавьте следующие строки:

```python
TELEGRAM_API_TOKEN = 'your_telegram_bot_token_here'
WEATHER_API_KEY = 'your_openweathermap_api_key_here'
```

Замените `your_telegram_bot_token_here` на токен вашего Telegram-бота и `your_openweathermap_api_key_here` на ваш API-ключ OpenWeatherMap.

## Использование

1. Запустите бота.

```bash
python your_script.py
```

2. В Telegram найдите вашего бота и отправьте команду `/start`, чтобы начать использование.

3. Введите название города, чтобы получить прогноз погоды.

## Зависимости

- `aiogram==3.11.0`
- `requests`

Убедитесь, что у вас установлена последняя версия `aiogram`, указанная в `requirements.txt`.

## Лицензия

Этот проект доступен по лицензии MIT. Подробности смотрите в файле LICENSE.
```

### Рекомендации:
- Замените `yourusername` и `yourrepository` на соответствующие значения, если вы планируете разместить проект на GitHub.
- Убедитесь, что файл `requirements.txt` содержит все необходимые зависимости. Например:
  ```
  aiogram==3.11.0
  requests
  ```
- Добавьте файл `LICENSE`, если вы хотите использовать определенную лицензию для вашего проекта.