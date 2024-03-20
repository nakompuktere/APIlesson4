from tools import download_images
import requests
import argparse


def fetch_spacex_last_launch(id):
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status()
    
    all_links = response.json()["links"]
    flickr = all_links["flickr"]
    links = flickr["original"]
    
    for index, item in enumerate(links):
        filename = f"images/spaceX_{index}.jpeg"
        download_images(filename, item)


def main():
    parser = argparse.ArgumentParser(description='Скачивает фотки из spaceX')
    parser.add_argument('--id', help='Ваш id', default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    
    fetch_spacex_last_launch(args.id)


if __name__ == "__main__":
    main()