# http://hubblesite.org/api/documentation
from utils import fetch_and_save_images
import requests
import os
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="Gets img dir and hubble collection"
    )
    parser.add_argument("-d", default="temp", dest="img_dir")
    parser.add_argument("-c", default="news", dest="collection")
    args = parser.parse_args()
    return (args.img_dir, args.collection)


def fetch_ids_from_image_collection(image_collection):
    url = "http://hubblesite.org/api/v3/images/"+image_collection
    return map(lambda x: x["id"], requests.get(url).json())


def fetch_hubble_images_links_by_id(id):
    url = "http://hubblesite.org/api/v3/image/"+str(id)
    return map(
        lambda x: x["file_url"],
        requests.get(url).json()["image_files"]
    )


def fetch_hubble_images_by_id(id, image_dir):
    hubble_imagelinks = fetch_hubble_images_links_by_id(id)
    fetch_and_save_images(hubble_imagelinks, image_dir)


def fetch_hubble_images_by_collection(
    image_collection="news",
    image_dir="temp"
):
    ids = tuple(fetch_ids_from_image_collection(image_collection))
    if not ids:
        return False
    for id in ids:
        fetch_hubble_images_by_id(id, image_dir)
    return True


if __name__ == "__main__":
    img_dir, img_collection = get_args()
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    if fetch_hubble_images_by_collection(img_collection, img_dir):
        print("→ Done")
    else:
        print("No images")
