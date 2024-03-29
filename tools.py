import requests
from pathlib import Path
from urllib.parse import urlparse
import os


def download_images(filename, url):
    Path("images").mkdir(parents=True, exist_ok=True)
    
    response = requests.get(url)
    response.raise_for_status()
    
    with open(filename, 'wb') as file:
      file.write(response.content)


def get_ext(url):
    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]

