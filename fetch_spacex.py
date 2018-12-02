### https://documenter.getpostman.com/view/2025350/RWaEzAiG#07a29989-38e3-47fb-9f64-c132b5842ff0
from utils import *


def fetch_spacex_last_launch_images(image_dir="temp"):
    latest_launch_url = "https://api.spacexdata.com/v3/launches/latest"
    image_links = fetch_json(latest_launch_url)["links"]["flickr_images"]
    fetch_and_save_images(image_links, image_dir)


def main():
    image_dir = input("► Type destination dir: ")
    fetch_spacex_last_launch_images(image_dir)


if __name__ == "__main__":
    main()
