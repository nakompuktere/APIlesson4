import requests
from tools import download_images
import os
from dotenv import load_dotenv


def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images?api_key="
    payload = {
        "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for index, epic_data in enumerate(response.json()):
        epic_image_name = epic_data["image"]
        epic_image_full_date = epic_data["date"]
        epic_image_date = epic_image_full_date[:10].replace("-", "/")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{epic_image_name}.png"
        file_paths = f"images/nasa_epic_{index}.png"
        download_images(file_paths, epic_url, api_key)


def main():
    load_dotenv()
    api_key = os.getenv("API_NASA_KEY")
    get_epic_images(api_key)


if __name__ == "__main__":
    main()
