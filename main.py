import datetime
import os
import requests
from dotenv import load_dotenv
import telegram
from os import listdir
import time
import random


def create_dirs(*args):
    for directory in args:
        os.makedirs(directory, exist_ok=True)


def download_image(url, full_image_name):

    response = requests.get(url)
    response.raise_for_status()

    with open(full_image_name, 'wb') as file:
        file.write(response.content)


def fetch_spacex_random_launch(spacex_dir):

    images_collection = []
    while len(images_collection) == 0:
        random_launch_num = random.randint(1, 110)
        spacex_url = f"https://api.spacexdata.com/v3/launches/" \
                     f"{random_launch_num}"

        response = requests.get(spacex_url)
        response.raise_for_status()

        images_collection = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(images_collection):
        image_full_path = f'{spacex_dir}spacex_{image_number}.jpg'
        download_image(image_url, image_full_path)


def download_nasa_daily_pics(nasa_token, nasa_pic_dir):

    pic_amount = 3
    params = {
        'count': pic_amount,
        'api_key': nasa_token
    }

    nasa_url = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(nasa_url,
                            params=params)
    response.raise_for_status()

    for pic_num, nasa_link in enumerate(response.json()):

        file_ext = os.path.splitext(nasa_link['url'])[1]

        date_time = datetime.datetime.fromisoformat(nasa_link['date'])
        day = '%02d' % date_time.day
        month = '%02d' % date_time.month
        year = date_time.year
        image_full_path = f'{nasa_pic_dir}apod_{year}-' \
                          f'{month}-{day}-{pic_num}{file_ext}'

        pic_link = nasa_link['url']

        download_image(pic_link, image_full_path)


def upload_images_to_telegram(telegram_token, chat_name, update_period):

    bot = telegram.Bot(token=telegram_token)
    chat_id = bot.get_chat(chat_name, timeout=100)['id']
    pic_path = "pics"

    for dir_counter in listdir(pic_path):
        for inner_pic_path in listdir(f'{pic_path}/{dir_counter}'):
            photo_path = f'{pic_path}/{dir_counter}/{inner_pic_path}'
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id=chat_id,
                               photo=photo,
                               timeout=2000)
            time.sleep(update_period)


def download_nasa_epics(nasa_token, epic_dir):

    epic_url = 'https://epic.gsfc.nasa.gov/api/images.php'
    file_ext = '.png'

    response = requests.get(epic_url)
    response.raise_for_status()

    for pic_num, nasa_link in enumerate(response.json()):

        date_time = datetime.datetime.fromisoformat(nasa_link['date'])
        day = '%02d' % date_time.day
        month = '%02d' % date_time.month
        year = date_time.year
        image_name = f'{epic_dir}EPIC_{year}-' \
                     f'{month}-{day}-{pic_num}{file_ext}'

        pic_link = f'https://epic.gsfc.nasa.gov/api/natural/date/' \
                   f'{year}{month}{day}{file_ext}'

        download_image(pic_link, image_name)


if __name__ == '__main__':

    load_dotenv()

    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_name = os.getenv("TELEGRAM_CHAT_NAME")
    update_period = int(os.getenv("TIMER_PERIOD", default=86400))

    spacex_dir = "pics/spacex_pic/"
    nasa_pic_dir = 'pics/daily_nasa/'
    epic_dir = 'pics/epics_nasa/'

    create_dirs(spacex_dir, nasa_pic_dir, epic_dir)

    while True:

        fetch_spacex_random_launch(spacex_dir)

        download_nasa_daily_pics(nasa_token, nasa_pic_dir)

        download_nasa_epics(epic_dir)

        upload_images_to_telegram(telegram_token, chat_name, update_period)
