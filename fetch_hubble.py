### http://hubblesite.org/api/documentation
from utils import fetch_and_save_images
import requests


def fetch_ids_from_image_collection(image_collection):
    url = "http://hubblesite.org/api/v3/images/"+image_collection
    return tuple(
        map(lambda x: x["id"], requests.get(url).json())
    )


def fetch_hubble_images_links_by_id(id):
    url = "http://hubblesite.org/api/v3/image/"+str(id)
    return tuple(
        map(lambda x: x["file_url"], requests.get(url).json()["image_files"])
    )


def fetch_hubble_images_by_id(id, image_dir):
    hubble_imagelinks = fetch_hubble_images_links_by_id(id)
    fetch_and_save_images(hubble_imagelinks, image_dir)


def fetch_hubble_images_by_collection(image_collection="news", image_dir="temp"):
    ids = fetch_ids_from_image_collection(image_collection)
    if ids:
        for id in ids:
            fetch_hubble_images_by_id(id, image_dir)
        return True
    else:
        return None
    


if __name__ == "__main__":
    img_dir = input("► Type destination dir: ")
    img_collection = input("► Type collection you want to download: ")
    try:
        if fetch_hubble_images_by_collection(img_collection, img_dir):
            print("→ Done")
        else:
            print("No images")
    except Exception as e:
        print(e)
