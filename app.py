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
movies_container = soup.find_all("li")

with open('./output.json', 'w') as file:
    for movie in movies_container[36:286]:
        link_movie: str = movie.a["href"]

        soup_link = BeautifulSoup(get_website(URL_DOMAIN + link_movie),
                                  "html.parser")

        movie_soup = Movie(soup_link)

        MOVIES.append(movie_soup.result)

    json.dump(MOVIES, file, indent=2)
