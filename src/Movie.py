from bs4 import BeautifulSoup
import logging
import requests


class Movie:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup
        self.logger = logging.getLogger(__name__)

    def get_title(self) -> str:
        return self.soup.select("div > h1 > span.sc-afe43def-1")[0].text

    def get_original_title(self) -> str:
        try:
            return self.soup.select("div > div.EpHJp")[0].text[16:]
        except IndexError:
            return self.get_title()

    def get_release_year(self) -> int:
        class_ = "ul.sc-afe43def-4.kdXikI a.ipc-link.ipc-link--baseAlt"
        release = int(self.soup.select(class_)[0].text)
        return release

    def get_parents_guide(self) -> str:
        class_ = \
            "ul > li > a.ipc-link.ipc-link--baseAlt.ipc-link--inherit-color"
        parents_guide = self.soup.select(class_)[5].text
        return parents_guide

    def get_duration(self) -> str:
        duration = self.soup.select("ul > li.ipc-inline-list__item")[6].text
        duration_str = duration.split(' ')
        return ''.join(duration_str)

    def get_imdb_rating(self) -> float:
        return \
          float(self.soup.select('div > span.sc-bde20123-1.iZlgcd')[0].text)

    def get_genre(self) -> list[str]:
        class_ = "div.ipc-chip-list__scroller > a > span.ipc-chip__text"
        genres = self.soup.select(class_)
        genres = self.clean_list_tags(genres)
        return genres

    def get_synopsis(self) -> str:
        return self.soup.select("p > span.sc-466bb6c-1.dRrIo")[0].text

    def get_director(self) -> list[str]:
        class_ = "a.ipc-metadata-list-item__label, " \
                "span.ipc-metadata-list-item__label, " \
                "a.ipc-metadata-list-item__list-content-item"
        end = 0
        tags = self.soup.select(class_)
        tags = self.clean_list_tags(tags)

        try:
            end = tags.index('Writers')
        except ValueError:
            end = tags.index('Writer')

        return tags[1:end]

    def get_writers(self) -> list[str]:
        class_ = "a.ipc-metadata-list-item__label, " \
                "span.ipc-metadata-list-item__label, " \
                "a.ipc-metadata-list-item__list-content-item"
        initial = 0
        tags = self.soup.select(class_)

        tags = self.clean_list_tags(tags)

        try:
            initial = tags.index('Writers') + 1
        except ValueError:
            initial = tags.index('Writer') + 1
        end = tags.index('Stars')

        return tags[initial:end]

    def get_stars(self) -> list[str]:
        class_ = "a.ipc-metadata-list-item__label, " \
            "span.ipc-metadata-list-item__label, " \
            "a.ipc-metadata-list-item__list-content-item"
        end = 0
        tags = self.soup.select(class_)
        tags = self.clean_list_tags(tags)
        initial = tags.index('Stars') + 1

        try:
            end = tags[1:].index('Directors') + 1
        except ValueError:
            end = tags[1:].index('Director') + 1

        return tags[initial:end]

    def get_ranking(self) -> int:
        try:
            class_ = 'div.sc-b45a339a-1.dBjmae a.top-rated-link'
            rate = self.soup.select(class_)[0].text
            return int(rate[17:])
        except IndexError:
            return 250

    def get_metascore(self) -> int | bool:
        try:
            metascore = self.soup.select('span.metacritic-score-box')[0].text
            return int(metascore)
        except IndexError:
            return False

    def clean_list_tags(self, tags) -> list[str]:
        data = []
        for tag in tags:
            data.append(tag.text)
        return data

    def result(self) -> object:
        try:
            infos = {
                "title": self.get_title(),
                "original_title": self.get_original_title(),
                "release_year": self.get_release_year(),
                "parents_guide": self.get_parents_guide(),
                "duration": self.get_duration(),
                "imdb_rating": self.get_imdb_rating(),
                "genre": self.get_genre(),
                "synopsis": self.get_synopsis(),
                "director": self.get_director(),
                "writers": self.get_writers(),
                "stars": self.get_stars(),
                "ranking_position": self.get_ranking(),
                "metascore": self.get_metascore(),
            }

            self.logger.info(f'{infos["title"]} was succesfully caught')
            self.logger.info(f'Position ranking: {infos["ranking_position"]}')
            self.logger.debug(infos)

            return infos
        except requests.HTTPError as e:
            self.logger.error('An error was finded')
            self.logger.error(e)
