from src.Movie import Movie
from src.request import get_website
from bs4 import BeautifulSoup

movie = get_website('https://www.imdb.com/title/tt0137523/?ref_=chttp_i_12')
soup = BeautifulSoup(movie, 'html.parser')
fight_club = Movie(soup)


def test_get_data_movie() -> None:
    s = "An insomniac office worker and a devil-may-care"
    s = s + " soap maker form an underground fight club that evolves into"
    s = s + " much more."
    assert fight_club.result() == {
        "title": "Clube da Luta",
        "original_title": "Fight Club",
        "release_year": 1999,
        "parents_guide": "18",
        "duration": "2h19m",
        "imdb_rating": 8.8,
        "genre": ['Drama'],
        "synopsis": s,
        "director": ['David Fincher'],
        "writers": ['Chuck Palahniuk', 'Jim Uhls'],
        "stars": ['Brad Pitt', 'Edward Norton', 'Meat Loaf'],
        "ranking_position": 12,
        "metascore": 67,
    }


def test_get_title() -> None:
    title = 'Clube da Luta'
    assert fight_club.get_title() == title


def test_get_original_title() -> None:
    original_title = 'Fight Club'
    assert fight_club.get_original_title() == original_title


def test_get_release_year() -> None:
    assert fight_club.get_release_year() == 1999


def test_get_parents_guide() -> None:
    assert fight_club.get_parents_guide() == '18'


def test_get_duration() -> None:
    assert fight_club.get_duration() == '2h19m'


def test_get_imdb_rating() -> None:
    assert fight_club.get_imdb_rating() == 8.8


def test_get_genre() -> None:
    genre = ['Drama']
    assert fight_club.get_genre() == genre


def test_get_synopsis() -> None:
    s = "An insomniac office worker and a devil-may-care"
    s = s + " soap maker form an underground fight club that evolves into"
    s = s + " much more."
    assert fight_club.get_synopsis() == s


def test_get_director() -> None:
    directors = ['David Fincher']
    assert fight_club.get_director() == directors


def test_get_writers() -> None:
    writers = ['Chuck Palahniuk', 'Jim Uhls']
    assert fight_club.get_writers() == writers


def test_get_stars() -> None:
    stars = ['Brad Pitt', 'Edward Norton', 'Meat Loaf']
    assert fight_club.get_stars() == stars


def test_get_ranking() -> None:
    assert fight_club.get_ranking() == 12


def test_get_metascore() -> None:
    assert fight_club.get_metascore() == 67


def test_clean_list_tags() -> None:
    tag = ['<li>Christian Bale</li>', '<li>Leo Dicaprio</li>',
           '<li>Elizabeth Olsen</li>']
    result = ['Christian Bale', 'Leo Dicaprio', 'Elizabeth Olsen']
    assert fight_club.clean_list_tags(tag) == result
