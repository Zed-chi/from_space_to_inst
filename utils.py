import requests
import os


def load_and_save_image(url, path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)


def fetch_json(url):
    res = requests.get(url)
    return res.json()


def get_name_from_url(url):
    return url.split("/")[-1]


def get_path(image_dir, name):
    return os.path.join(image_dir, name)


def fetch_and_save_images(links, image_dir):
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    for link in links:
        name = get_name_from_url(link)
        # из-за большого размера файла ввел возможность выбора
        if input("→ Load {}?(Y/N): ".format(name)).upper() == "Y":
            path = get_path(image_dir, name)
            print("\t╟ loading {}".format(link))
            load_and_save_image(link, path)
            print("\t╚ done")
