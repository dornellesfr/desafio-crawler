from bs4 import BeautifulSoup
from request import get_website


def clean_list_tags(tags) -> list[str]:
    data = []
    for tag in tags:
        data.append(tag.text)
    return data


def get_release_year(soup: BeautifulSoup) -> int:
    class_ = "ul > li > a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color"
    release = int(soup.select(class_)[4].text)
    return release


def get_parents_guide(soup: BeautifulSoup) -> int:
    class_ = "ul > li > a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color"
    parents_guide = int(soup.select(class_)[5].text)
    return parents_guide


def get_duration(soup: BeautifulSoup) -> str:
    duration = soup.select("ul > li.ipc-inline-list__item")[6].text
    duration_str = duration.split(' ')
    return ''.join(duration_str)


def get_genre(soup: BeautifulSoup) -> list[str]:
    class_ = "div.ipc-chip-list__scroller > a > span.ipc-chip__text"
    genres = soup.select(class_)
    genres = clean_list_tags(genres)
    return genres


def get_director(soup: BeautifulSoup) -> list[str]:
    class_ = "a.ipc-metadata-list-item__label, " \
             "span.ipc-metadata-list-item__label, " \
             "a.ipc-metadata-list-item__list-content-item"
    end = 0
    tags = soup.select(class_)
    tags = clean_list_tags(tags)

    try:
        end = tags.index('Writers')
    except ValueError:
        end = tags.index('Writer')

    return tags[1:end]


def get_writers(soup: BeautifulSoup) -> list[str]:
    class_ = "a.ipc-metadata-list-item__label, " \
            "span.ipc-metadata-list-item__label, " \
            "a.ipc-metadata-list-item__list-content-item"
    initial = 0
    tags = soup.select(class_)

    tags = clean_list_tags(tags)

    try:
        initial = tags.index('Writers') + 1
    except ValueError:
        initial = tags.index('Writer') + 1
    end = tags.index('Stars')

    return tags[initial:end]


def get_stars(soup: BeautifulSoup) -> list[str]:
    class_ = "a.ipc-metadata-list-item__label, " \
        "span.ipc-metadata-list-item__label, " \
        "a.ipc-metadata-list-item__list-content-item"
    end = 0
    tags = soup.select(class_)

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


def get_popularity(soup: BeautifulSoup) -> int:
    popularity = soup.select("div > div.sc-5f7fb5b4-1.bhuIgW")[0].text
    popularity = popularity.replace(',', '')
    return int(popularity)


def get_metascore(soup: BeautifulSoup) -> int:
    metascore = soup.select('span.metacritic-score-box')[0].text
    return int(metascore)


def get_original_country(soup: BeautifulSoup) -> str:
    class_ = "div.fVkLRr a.ipc-metadata-list-item__list-content-item"
    country = soup.select(class_)[1].text
    return country


def scraping_movie(link: str):
    html_content = get_website(link)
    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.select("div > h1 > span.sc-afe43def-1")[0].text
    original_title = soup.select("div > div.sc-afe43def-3.EpHJp")[0].text[16:]
    release_year = get_release_year(soup)
    parents_guide = get_parents_guide(soup)
    duration = get_duration(soup)
    imdb_rating = float(soup.select('div > span.sc-bde20123-1.iZlgcd')[0].text)
    popularity = get_popularity(soup)
    genre = get_genre(soup)
    synopsis = soup.select("p > span.sc-466bb6c-1.dRrIo")[0].text
    director = get_director(soup)
    writers = get_writers(soup)
    stars = get_stars(soup)
    ranking_position = get_ranking(soup)
    metascore = get_metascore(soup)
    original_country = get_original_country(soup)

    infos = {
        "title": title,
        "original_title": original_title,
        "release_year": release_year,
        "parents_guide": parents_guide,
        "duration": duration,
        "imdb_rating": imdb_rating,
        "popularity": popularity,
        "genre": genre,
        "synopsis": synopsis,
        "director": director,
        "writers": writers,
        "stars": stars,
        "ranking_position": ranking_position,
        "metascore": metascore,
        "original_country": original_country,
    }

    return infos


if __name__ == "__main__":
    r = scraping_movie('https://www.imdb.com/title/tt9362722/?ref_=chttp_t_24')
    print(r)
