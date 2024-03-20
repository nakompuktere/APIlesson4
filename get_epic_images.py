import requests
from tools import download_images
import argparse


def get_epic_images(api_key):
    url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    for index, epic_image_inf in enumerate(response.json()):
        epic_image_name = epic_image_inf["image"]
        epic_image_full_date = epic_image_inf["date"]
        epic_image_date = epic_image_full_date[:10].replace("-", "/")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{epic_image_name}.png?api_key={api_key}"
        filename = f"images/nasa_epic_{index}.png"
        download_images(filename, epic_url)


def main():
    parser = argparse.ArgumentParser(description='Скачивает фотки EPIC из NASA')
    parser.add_argument('api_key', help='ваш API ключ')
    args = parser.parse_args()
    get_epic_images(args.api_key)


if __name__ == "__main__":
    main()
