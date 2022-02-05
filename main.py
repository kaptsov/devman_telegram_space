import datetime

import os
import requests
from dotenv import load_dotenv

import telegram


def download_image(url, directory, filename):

    if not os.path.exists(directory):
        os.makedirs(directory)

    response = requests.get(url)
    response.raise_for_status()

    full_filename = directory + filename
    with open(full_filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, directory):

    response = requests.get(url)
    response.raise_for_status()

    images_list = response.json()['links']['flickr_images']

    for image_number, image_url in enumerate(images_list):
        image_name = f'spacex_{image_number}.jpg'
        download_image(image_url, directory, image_name)


def download_nasa_pics(url_list, directory, is_it_epic):

    load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    nasa_pic_count = 3
    data = f'count={nasa_pic_count}'

    response = requests.get(url_list+nasa_token, params=data)
    response.raise_for_status()

    for nasa_num, nasa_link in enumerate(response.json()):

        if is_it_epic:
            file_ext = '.png'
        else:
            file_ext = os.path.splitext(nasa_link['url'])[1]

        date_time = datetime.datetime.fromisoformat(nasa_link['date'])
        day = '%02d' % date_time.day
        month = '%02d' % date_time.month
        year = date_time.year

        image_name = f'{directory[:5]}_{year}-' \
                     f'{month}-{day}-{nasa_num}{file_ext}'

        if is_it_epic:
            pic_link = f'https://api.nasa.gov/EPIC/archive/natural/' \
                       f'{year}/{month}/{day}/png/{nasa_link["image"]}.png?api_key=' \
                       f'{nasa_token}'
        else:
            pic_link = nasa_link['url']

        download_image(pic_link, directory, image_name)


if __name__ == '__main__':

    load_dotenv()
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = telegram.Bot(token=telegram_token)

    print(bot.get_me())
    updates = bot.get_updates()
    print(updates[0])
    bot.send_message(text='Привет, Оля!', chat_id=-1001681623193)

    spacex_dir = "spacex_pic/"
    spacex_url = "https://api.spacexdata.com/v3/launches/67"
    fetch_spacex_last_launch(spacex_url, spacex_dir)

    nasa_pic_dir = 'daily_nasa/'
    nasa_url = 'https://api.nasa.gov/planetary/apod?api_key='
    download_nasa_pics(nasa_url, nasa_pic_dir, False)

    nasa_epic_dir = 'epics_nasa/'
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural?api_key='
    download_nasa_pics(nasa_epic_url, nasa_epic_dir, True)


