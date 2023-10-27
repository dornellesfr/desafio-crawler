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


def find_by_tag(soup: BeautifulSoup, tag: str, attr: str, value: str, index=0) -> str:
    item = []
    if index != 0:
        item = soup.find_all(
            tag,
            {attr: value}
        )
    else:
        data = soup.find(
            tag,
            {attr: value}
        )
        item.append(data)

    if item:
        return item[index].text
    return "Unknow"


def scraping_movie(link: str):
    movie_data = {}

    html_content = get_website(link)
    soup = BeautifulSoup(html_content, "html.parser")

    title = find_by_tag(soup, "span", "class", "sc-afe43def-1 fDTGTb")
    original_title = find_by_tag(soup, "div", "class", "sc-afe43def-3 EpHJp")[16:]
    release_year = find_by_tag(soup, "a", "class", "ipc-link ipc-link--baseAlt ipc-link--inherit-color", 5)
    parents_guide = find_by_tag(soup, "a", "class", "ipc-link ipc-link--baseAlt ipc-link--inherit-color", 6)
    duration = find_by_tag(soup, "li", "class", "ipc-inline-list__item", 6)
    imdb_rating = find_by_tag(soup, "span", "class", "sc-bde20123-1 iZlgcd")
    popularity = find_by_tag(soup, "div", "class", "sc-5f7fb5b4-1 bhuIgW")
    genre = find_by_tag(soup, "")

    print(title)
    print(original_title)
    print(release_year)
    print(parents_guide)
    print(duration)
    print(imdb_rating)
    print(popularity)
    print(genre)
    


if __name__ == "__main__":
    scraping_movie('https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2')
