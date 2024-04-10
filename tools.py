import requests
from pathlib import Path
from urllib.parse import urlparse
import os


def download_images(file_paths, urls, api_key=""):
    Path("images").mkdir(parents=True, exist_ok=True)
    
    payload = {
      "api_key": api_key
    }
    response = requests.get(urls, params=payload)
    response.raise_for_status()
    
    with open(file_paths, 'wb') as file:
      file.write(response.content)


def get_ext(urls):
    parsed_urls = urlparse(urls)
    return os.path.splitext(parsed_urls.path)[1]

