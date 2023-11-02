import json
from bs4 import BeautifulSoup
import pdfkit
from src.request import get_website
from src.Movie import Movie

URL_DOMAIN = "https://www.imdb.com"
URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
IMG = pdfkit.from_url(URL, 'screenshot.pdf')
MOVIES = []

html_content = get_website(URL)

if html_content is None:
    raise TimeoutError

soup = BeautifulSoup(html_content, "html.parser")
movies_container = soup.select("li.jemTre.cli-parent a.ipc-title-link-wrapper")

for movie in movies_container:
    link = movie['href']
    movie_link = get_website(URL_DOMAIN + str(link))
    soup_ = BeautifulSoup(movie_link, "html.parser")
    movie_soup = Movie(soup_)
    MOVIES.append(movie_soup.result())

with open('./output.json', 'w') as file:
    json.dump(MOVIES, file, indent=2)
