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


def get_tag_data(soup: BeautifulSoup, tag: str, attr: str, value: str):
    item = soup.find(
        tag,
        {attr: value})
    if item:
        return item.text
    return "Unknow"


def scraping_movie(link: str):
    movie_data = {}

    html_content = get_website(link)
    soup = BeautifulSoup(html_content, "html.parser")

    title = get_tag_data(soup, "span", "class", "sc-afe43def-1 fDTGTb")
    original_title = get_tag_data(soup, "div", "class", "sc-afe43def-3 EpHJp")[16:]
    release_year = get_tag_data(soup, "a", "href", "/title/tt0068646/releaseinfo?ref_=tt_ov_rdat")

    print(title)
    print(original_title)
    print(release_year)


if __name__ == "__main__":
    scraping_movie('https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2')
