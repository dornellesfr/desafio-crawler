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


def clean_list_tags(tags) -> list[str]:
    data = []
    for tag in tags:
        data.append(tag.text)
    return data


def get_duration(soup: BeautifulSoup) -> str:
    duration = soup.select("ul > li.ipc-inline-list__item")[6].text
    duration_str = duration.split(' ')
    return ''.join(duration_str)


def get_genre(soup: BeautifulSoup) -> list[str]:
    genres = soup.select("div.ipc-chip-list__scroller > a > span.ipc-chip__text")
    genres = clean_list_tags(genres)
    return genres


def get_director(soup: BeautifulSoup) -> list[str]:
    end = 0
    tags = soup.select("a.ipc-metadata-list-item__label.ipc-metadata-list-item__label--link, span.ipc-metadata-list-item__label.ipc-metadata-list-item__label--btn, a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link")
    tags = clean_list_tags(tags)

    try:
        end = tags.index('Writers')
    except ValueError:
        end = tags.index('Writer')

    return tags[1:end]


def get_writers(soup: BeautifulSoup) -> list[str]:
    initial = 0
    tags = soup.select("a.ipc-metadata-list-item__label.ipc-metadata-list-item__label--link, span.ipc-metadata-list-item__label.ipc-metadata-list-item__label--btn, a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link")

    tags = clean_list_tags(tags)

    try:
        initial = tags.index('Writers') + 1
    except ValueError:
        initial = tags.index('Writer') + 1
    end = tags.index('Stars')

    return tags[initial:end]


def get_stars(soup: BeautifulSoup) -> list[str]:
    end = 0
    tags = soup.select("a.ipc-metadata-list-item__label.ipc-metadata-list-item__label--link, span.ipc-metadata-list-item__label.ipc-metadata-list-item__label--btn, a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link")

    tags = clean_list_tags(tags)

    initial = tags.index('Stars') + 1

    try:
        end = tags[1:].index('Directors') + 1
    except ValueError:
        end = tags[1:].index('Director') + 1

    return tags[initial:end]


def get_ranking(soup: BeautifulSoup) -> int:
    rate = soup.select("div.sc-fcdc3619-1 > a.ipc-link")[0].text
    return int(rate[17:])


def get_metascore(soup: BeautifulSoup) -> int:
    ...


def get_storyline(soup: BeautifulSoup) -> str:
    ...


def get_country_of_origin(soup: BeautifulSoup) -> str:
    ...


def get_budget(soup: BeautifulSoup) -> int:
    ...


def get_gross_worldwide(soup: BeautifulSoup) -> int:
    ...


def scraping_movie(link: str):
    # movie_data = {}

    html_content = get_website(link)
    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.select("div > h1 > span.sc-afe43def-1")[0].text
    original = soup.select("div > div.sc-afe43def-3.EpHJp")[0].text[16:]
    release_year = int(soup.select("ul > li > a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color")[4].text)
    parents_guide = int(soup.select("ul > li > a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color")[5].text)
    duration = get_duration(soup)
    imdb_rating = float(soup.select('div > span.sc-bde20123-1.iZlgcd')[0].text)
    # popularity = float(soup.select("div > div.sc-5f7fb5b4-1.bhuIgW")[0].text)
    genre = get_genre(soup)
    synopsis = soup.select("p > span.sc-466bb6c-1.dRrIo")[0].text
    director = get_director(soup)
    writers = get_writers(soup)
    stars = get_stars(soup)
    rate_movie = get_ranking(soup)
    # metascore = get_storyline (soup)
    # storyline = get_storyline (soup)
    # country_of_origin = get_country_of_origin(soup)
    # budget = get_budget(soup)
    # gross_worldwide = get_gross_worldwide(soup)

    print(title)
    print(original)
    print(release_year)
    print(parents_guide)
    print(duration)
    print(imdb_rating)
    # print(popularity)
    print(genre)
    print(synopsis)
    print(director)
    print(writers)
    print(stars)
    print(rate_movie)
    print(metascore)
    # print(storyline)
    # print(country_of_origin)
    # print(budget)
    # print(gross_worldwide)


if __name__ == "__main__":
    scraping_movie('https://www.imdb.com/title/tt0211915/?ref_=chttp_t_105')
