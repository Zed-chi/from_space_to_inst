import os
import argparse
from instabot import Bot
from dotenv import load_dotenv
from fetch_hubble import fetch_hubble_images_by_collection
from fetch_spacex import fetch_spacex_last_launch_images


def get_args():
    parser = argparse.ArgumentParser(
        description="Gets img dir and hubble collection"
    )
    parser.add_argument("-d", default="temp", dest="img_dir")
    parser.add_argument("-c", default="news", dest="collection")
    args = parser.parse_args()
    return (args.img_dir, args.collection)


def upload_images_to_instagram(bot, image_dir):
    images = filter(lambda x: x.endswith(".jpg"), os.listdir(image_dir))
    for image in images:
        bot.upload_photo(os.path.join(image_dir, image))


if __name__ == "__main__":
    load_dotenv()
    login = os.getenv("inst_login")
    pas = os.getenv("inst_pass")
    img_dir, hubble_collection = get_args()
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    if fetch_spacex_last_launch_images(img_dir):
        print("Spaceximages fetched")
    else:
        print("No images")
    if fetch_hubble_images_by_collection(hubble_collection, img_dir):
        print("Hubble images fetched")
    else:
        print("No images")
    user = Bot()
    user.login(username=login, password=pas)
    upload_images_to_instagram(user, img_dir)
