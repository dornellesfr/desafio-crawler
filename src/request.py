import requests


def get_website(link):
    try:
        return requests.get(link, timeout=4)
    except requests.ReadTimeout:
        return requests.get(link, timeout=6)
