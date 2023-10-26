import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}


def get_website(link):
    try:
        response = requests.get(link, headers=header, timeout=4)
        response.raise_for_status()
        print(response.status_code)
        return response.text
    except requests.HTTPError as e:
        print(f"Error: {e}")
        return None
