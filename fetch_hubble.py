# http://hubblesite.org/api/documentation
from utils import fetch_and_save_images
import requests
import os


def fetch_ids_from_image_collection(image_collection):
    url = "http://hubblesite.org/api/v3/images/"+image_collection
    # tuple/list требуется для проверки на истинность
    return tuple(map(lambda x: x["id"], requests.get(url).json()))


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
    ids = fetch_ids_from_image_collection(image_collection)
    if not ids:
        return False
    for id in ids:
        fetch_hubble_images_by_id(id, image_dir)
    return True


if __name__ == "__main__":
    img_dir = input("► Type destination dir: ")
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)    
    img_collection = input("► Type collection you want to download: ")
    if fetch_hubble_images_by_collection(img_collection, img_dir):
        print("→ Done")
    else:
        print("No images")
