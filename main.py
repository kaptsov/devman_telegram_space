import datetime
import os
import requests
from dotenv import load_dotenv
import telegram
from os import listdir
import time
import random


def download_image(url, directory, image_name):

    os.makedirs(directory, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    full_image_name = f'{directory}{image_name}'
    with open(full_image_name, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():

    launch_rand_num = random.randint(1, 110)
    spacex_dir = "pics/spacex_pic/"
    spacex_url = f"https://api.spacexdata.com/v3/" \
                 f"launches/{launch_rand_num}"

    response = requests.get(spacex_url)
    response.raise_for_status()

    images_list = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(images_list):
        image_name = f'spacex_{image_number}.jpg'
        download_image(image_url, spacex_dir, image_name)


def download_nasa_daily_pics(nasa_token):

    pic_amount = 3
    params = {
        'count': pic_amount,
        'api_key': nasa_token
    }

    nasa_pic_dir = 'pics/daily_nasa/'
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
        image_name = f'{nasa_pic_dir[5:10]}_{year}-' \
                     f'{month}-{day}-{pic_num}{file_ext}'

        pic_link = nasa_link['url']

        download_image(pic_link, nasa_pic_dir, image_name)


def upload_images(telegram_token, chat_name, update_period):

    bot = telegram.Bot(token=telegram_token)
    chat_id = bot.get_chat(chat_name, timeout=100)['id']
    pic_path = "pics"

    for dir_counter in listdir(pic_path):
        for inner_pic_path in listdir(f'{pic_path}/{dir_counter}'):
            photo_path = f'{pic_path}/{dir_counter}/{inner_pic_path}'
            bot.send_photo(chat_id=chat_id,
                           photo=open(photo_path, 'rb'),
                           timeout=2000)
            time.sleep(update_period)


def download_nasa_epics(nasa_token):

    epic_dir = 'pics/epics_nasa/'
    epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    file_ext = '.png'
    params = {
        'api_key': nasa_token
    }

    response = requests.get(epic_url, params=params)
    response.raise_for_status()

    for pic_num, nasa_link in enumerate(response.json()):

        date_time = datetime.datetime.fromisoformat(nasa_link['date'])
        day = '%02d' % date_time.day
        month = '%02d' % date_time.month
        year = date_time.year
        image_name = f'{epic_dir[5:10]}_{year}-' \
                     f'{month}-{day}-{pic_num}{file_ext}'

        pic_link = f'https://api.nasa.gov/EPIC/archive/natural/' \
                   f'{year}/{month}/{day}/png/{nasa_link["image"]}' \
                   f'.png?api_key={nasa_token}'

        download_image(pic_link, epic_dir, image_name)


if __name__ == '__main__':

    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_name = os.getenv("TELEGRAM_CHAT_NAME")
    update_period = int(os.getenv("TIMER_PERIOD", default=86400))

    while(True):

        fetch_spacex_last_launch()

        download_nasa_daily_pics(nasa_token)

        download_nasa_epics(nasa_token)

        upload_images(telegram_token, chat_name, update_period)
