import requests
import argparse
from tools import download_images, get_ext
import os
from dotenv import load_dotenv


def downloads_nasa_apod(count, api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    payload = {"count": count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, image_inf in enumerate(response.json()):
        image_url = image_inf["url"]
        extension = get_ext(image_url)
        if extension != "":
            filename = f"images/nasa_apod_{index}{extension}"
            download_images(filename, image_url)

def main():
    load_dotenv()
    api_key = os.getenv("API_NASA_KEY")
    parser = argparse.ArgumentParser(description='Скачивает фотки APOD из NASA')
    parser.add_argument('--count', help='количество фото', default=30)
    args = parser.parse_args()
    downloads_nasa_apod(args.count, api_key)


if __name__ == "__main__":
    main()
