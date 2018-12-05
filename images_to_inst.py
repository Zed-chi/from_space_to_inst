import os
from instabot import Bot
from dotenv import load_dotenv
from fetch_hubble import fetch_hubble_images_by_collection
from fetch_spacex import fetch_spacex_last_launch_images


def upload_images_to_instagram(bot, image_dir):
    images = tuple(filter(lambda x: x.endswith(".jpg"), os.listdir(image_dir)))
    for image in images:
        bot.upload_photo(os.path.join(image_dir, image))


if __name__ == "__main__":
    load_dotenv()
    name = os.getenv("login")
    pas = os.getenv("password")
    img_dir = "images"
    hubble_collection = input("Type image collection: ")
    try:
        if fetch_spacex_last_launch_images(img_dir):
            print("Spaceximages fetched")
        else:
            print("No images")
        if fetch_hubble_images_by_collection(hubble_collection, img_dir):
            print("Hubble images fetched")
        else:
            print("No images")
        user = Bot()
        user.login(username=name, password=pas)
        upload_images_to_instagram(user, img_dir)
    except Exception as e:
        print(e)
