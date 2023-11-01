import requests
import logging

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

logging.basicConfig(filename='scraper.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def get_website(link: str):
    try:
        response = requests.get(link, headers=header, timeout=4)
        response.raise_for_status()
        logger.info(f'Site status code: {response.status_code}')
        return response.text
    except requests.ReadTimeout:
        response = requests.get(link, headers=header, timeout=10)
        logger.info(f'Site status code: {response.status_code}')
        return response.text
