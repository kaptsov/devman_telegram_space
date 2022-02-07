# Space Telegram

The script downloads photos to the local "pics" folder, and then publishes them through the bot to the telegram group.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

For the script to work, create the **".env"** file in the project folder, in which you need to create variables:

```
NASA_TOKEN="token"
TELEGRAM_BOT_TOKEN="token"
TELEGRAM_CHAT_NAME="@telegramchannelname"
TIMER_PERIOD=[sec]
```

To get **NASA_TOKEN** you need to register [following the link](https://api.nasa.gov/#apod). This will give you the NASA API KEY, which you need to insert in quotes into the ".env" file.

To get **TELEGRAM_BOT_TOKEN** you need to learn how to create bots in telegrams and get an API key [link](https://core.telegram.org/bots).

The **TIMER_PERIOD** variable is responsible for the time interval between photo publications. The default value is 84300 (seconds) if no value is specified. But if you want faster, change the value to the desired number of seconds.

Add the created bot to administrators in your telegram channel.

In the **TELEGRAM_CHAT_NAME** variable, put the name of your channel, in the form "@channel"

Then write in the console:

```
python main.py
```

The script will run, first download photos to the "pics" directory and then you will see how the bot will upload photos one by one to the channel with a frequency of **TIMER_PERIOD**.


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

# Космический Телеграм

Скрипт выкачивает фотографии в локальную папку "pics", и затем публикует через бота в телеграмм в группу.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для работы скрипта следует в папке с проектом создать файл **".env"**, в котором необходимо создать переменные:

```
NASA_TOKEN="token"
TELEGRAM_BOT_TOKEN="token"
TELEGRAM_CHAT_NAME="@telegramchannelname"
TIMER_PERIOD=[sec]
```

Чтобы получить **NASA_TOKEN** необходимо зарегистрироваться [по ссылке](https://api.nasa.gov/#apod). Так вы получите NASA API KEY, который нужно в кавычках вставить в файл ".env".

Чтобы получить **TELEGRAM_BOT_TOKEN** необходимо ознакомиться как создавать ботов в телеграм и получать ключ API [по ссылке](https://core.telegram.org/bots).

Переменная **TIMER_PERIOD** отвечает за интервал времени между публикациями фотографий. По умолчанию стоит значени 84300 (секунд), если никакое значение не указывать. Но если хочется быстрее, измените значение на нужное количество секунд.

В ваш канал в телеграмме добавьте созданного бота в администраторы.

В переменную **TELEGRAM_CHAT_NAME** следует поместить имя вашего канала, в виде "@channel"

Затем в консоли прописать:

```
python main.py
```

Скрипт запустится, сначала скачает фотографии в директорию "pics" а затем вы увидите, как бот будет загружать фотографии по одной в канал с периодичностью **TIMER_PERIOD**.


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
