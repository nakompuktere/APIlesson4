import requests
from tools import download_images
import os
from dotenv import load_dotenv


def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, epic in enumerate(response.json()):
        epic_image_name = epic["image"]
        epic_image_full_date = epic["date"]
        epic_image_date = epic_image_full_date[:10].replace("-", "/")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{epic_image_name}.png"
        file_path = f"images/nasa_epic_{index}.png"
        download_image(file_path, epic_url, api_key)


def main():
    load_dotenv()
    api_key = os.getenv("API_NASA_KEY")
    get_epic_images(api_key)


if __name__ == "__main__":
    main()
