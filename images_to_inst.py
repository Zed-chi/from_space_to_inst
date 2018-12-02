import os
from instabot import Bot
from fetch_hubble import fetch_hubble_images_by_collection
from fetch_spacex import fetch_spacex_last_launch_images


def upload_images_to_instagram(user, image_dir):
    images = tuple(filter(lambda x: x.endswith(".jpg"), os.listdir(image_dir)))
    for image in images:
        user.upload_photo(os.path.join(image_dir, image))
    print("→ Done")


def main():
    image_dir = "images"
    hubble_collection = "spacecraft"
    fetch_spacex_last_launch_images(image_dir)
    fetch_hubble_images_by_collection(hubble_collection, image_dir)
    user = Bot()
    user.login()
    upload_images_to_instagram(user, image_dir)


if __name__ == "__main__":
    main()
