# Space Telegram

The script downloads photos to the local "pics" folder, and then publishes them through the bot to the telegram group.

### How to install

For the script to work, you should create a **".env"** file, in which you need to create three variables:

```
NASA_TOKEN="token"
TELEGRAM_BOT_TOKEN="token"
TIMER_PERIOD=[sec]
```

To get **NASA_TOKEN** you need to register [following the link](https://api.nasa.gov/#apod). This will give you the NASA API KEY, which you need to insert in quotes into the ".env" file.

To get **TELEGRAM_BOT_TOKEN** you need to learn how to create bots in telegrams and get an API key [link](https://core.telegram.org/bots).

The **TIMER_PERIOD** variable is responsible for the time interval between photo publications. The default value is 84300 (seconds) if no value is specified. But if you want faster, change the value to the desired number of seconds.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

# Космический Телеграм

Скрипт выкачивает фотографии в локальную папку "pics", и затем публикует через бота в телеграмм в группу.

### Как установить

Для работы скрипта следует создать файл **".env"**, в котором необходимо создать три переменные:

```
NASA_TOKEN="token"
TELEGRAM_BOT_TOKEN="token"
TIMER_PERIOD=[sec]
```

Чтобы получить **NASA_TOKEN** необходимо зарегистрироваться [по ссылке](https://api.nasa.gov/#apod). Так вы получите NASA API KEY, который нужно в кавычках вставить в файл ".env".

Чтобы получить **TELEGRAM_BOT_TOKEN** необходимо ознакомиться как создавать ботов в телеграм и получать ключ API [по ссылке](https://core.telegram.org/bots).

Переменная **TIMER_PERIOD** отвечает за интервал времени между публикациями фотографий. По умолчанию стоит значени 84300 (секунд), если никакое значение не указывать. Но если хочется быстрее, измените значение на нужное количество секунд.


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
