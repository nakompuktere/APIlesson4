import requests
from pathlib import Path
from urllib.parse import urlparse
import os


#filename = "images/hubble.jpeg"
# id = "5eb87d47ffd86e000604b38a"
# api_key = os.environ['API_NASA_KEY']
# url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
# url_two = f"https://api.spacexdata.com/v5/launches/{id}"
# url_three = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
# url_four = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}"


def download_images(filename, url):
    Path("images").mkdir(parents=True, exist_ok=True)
    
    response = requests.get(url)
    response.raise_for_status()
    
    with open(filename, 'wb') as file:
      file.write(response.content)


def get_ext(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]

