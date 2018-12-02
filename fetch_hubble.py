### http://hubblesite.org/api/documentation
from utils import *


def fetch_ids_from_image_collection(collection):
    url = "http://hubblesite.org/api/v3/images/"+collection
    return tuple(
        map(lambda x: x["id"], fetch_json(url))
    )


def fetch_hubble_images_links_by_id(id):
    url = "http://hubblesite.org/api/v3/image/"+str(id)
    return tuple(
        map(lambda x: x["file_url"], fetch_json(url)["image_files"])
    )


def fetch_hubble_images_by_id(id, image_dir):
    hubble_imagelinks = fetch_hubble_images_links_by_id(id)
    fetch_and_save_images(hubble_imagelinks, image_dir)


def fetch_hubble_images_by_collection(collection="news", image_dir="temp"):
    ids = fetch_ids_from_image_collection(collection)
    for id in ids:
        fetch_hubble_images_by_id(id, image_dir)
    print("→ Done")


def main(image_dir="temp"):
    image_dir = input("► Type destination dir: ")
    collection = input("► Type collection you want to download: ")
    fetch_hubble_images_by_collection(collection, image_dir)


if __name__ == "__main__":
    main()
