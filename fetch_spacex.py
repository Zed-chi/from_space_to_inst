'''
https://documenter.getpostman.com/
view/2025350/RWaEzAiG#07a29989-38e3-47fb-9f64-c132b5842ff0
'''
from utils import fetch_and_save_images
import requests


def fetch_spacex_last_launch_images(image_dir="temp"):
    latest_launch_url = "https://api.spacexdata.com/v3/launches/latest"
    image_links =\
        requests.get(latest_launch_url).json()["links"]["flickr_images"]
    if not image_links:
        return False
    fetch_and_save_images(image_links, image_dir)
    return True


if __name__ == "__main__":
    img_dir = input("► Type destination dir: ")
    if fetch_spacex_last_launch_images(img_dir):
        print("→ Done")
    else:
        print("→ No images")
