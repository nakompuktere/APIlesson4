import requests
from pathlib import Path
from urllib.parse import urlparse
import os


def download_image(file_path, url, api_key=""):
    Path("images").mkdir(parents=True, exist_ok=True)
    
    payload = {
      "api_key": api_key
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    
    with open(file_path, 'wb') as file:
      file.write(response.content)


def get_ext(url):
    parsed_urls = urlparse(url)
    return os.path.splitext(parsed_urls.path)[1]

