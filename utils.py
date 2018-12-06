import requests
import os


def load_and_save_image(url, path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)


def fetch_and_save_images(links, image_dir):
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    for link in links:
        name = link.split("/")[-1]
        # из-за большого размера файла ввел возможность выбора
        if input("→ Load {}?(Y/N): ".format(name)).upper() == "Y":
            path = os.path.join(image_dir, name)
            load_and_save_image(link, path)
