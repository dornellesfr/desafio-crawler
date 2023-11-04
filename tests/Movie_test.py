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
        "popularity": 132,
        "genre": ['Drama'],
        "synopsis": s,
        "director": ['David Fincher'],
        "writers": ['Chuck Palahniuk', 'Jim Uhls'],
        "stars": ['Brad Pitt', 'Edward Norton', 'Meat Loaf'],
        "ranking_position": 12,
        "metascore": 67,
        "original_country": "Germany",
    }
