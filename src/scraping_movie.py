from bs4 import BeautifulSoup
from request import get_website


keys_data = [
    "title",
    "original_title",
    "release_year",
    "parents_guide",
    "duration",
    "imdb_rating",
    "popularity",
    "genre",
    "description",
    "synopsis",
    "director",
    "writers",
    "stars",
    "oscars_won",
    "storyline",
    "country_of_origin",
    "budget",
    "gross_worldwide",
]


def get_title(soup: BeautifulSoup) -> str:
    title = soup.find(
        "span",
        {"class": "sc-afe43def-1 fDTGTb"})
    if title:
        return title.text
    return "Unknow"

def get_original_title()


def scraping_movie(link: str):
    movie_data = {}

    html_content = get_website(link)
    soup = BeautifulSoup(html_content, "html.parser")

    print(get_title(soup))


if __name__ == "__main__":
    scraping_movie('https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2')
