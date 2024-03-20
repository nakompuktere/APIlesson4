import requests
import argparse
from tools import download_images, get_ext


def downloads_nasa_apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    payload = {"count": 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, image_inf in enumerate(response.json()):
        image_url = image_inf["url"]
        extension = get_ext(image_url)
        filename = f"images/nasa_apod_{index}{extension}"
        download_images(filename, image_url)

def main():
    parser = argparse.ArgumentParser(description='Скачивает фотки APOD из NASA')
    parser.add_argument('api_key', help='Ваш API ключ')
    args = parser.parse_args()
    downloads_nasa_apod(args.api_key)


if __name__ == "__main__":
    main()
