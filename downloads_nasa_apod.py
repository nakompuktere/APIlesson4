import requests
import argparse
from tools import download_images, get_ext
import os
from dotenv import load_dotenv


def downloads_nasa_apod(count, api_key):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "count": count,
        "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, apod in enumerate(response.json()):
        image_urls = apod["url"]
        extension = get_ext(image_urls)
        if extension:
            file_paths = f"images/nasa_apod_{index}{extension}"
            download_images(file_paths, image_urls, api_key)

def main():
    load_dotenv()
    api_key = os.getenv("API_NASA_KEY")
    parser = argparse.ArgumentParser(description='Скачивает фотки APOD из NASA')
    parser.add_argument('--count', help='количество фото', default=30, type=int)
    args = parser.parse_args()
    downloads_nasa_apod(args.count, api_key)


if __name__ == "__main__":
    main()