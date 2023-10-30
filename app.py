from bs4 import BeautifulSoup
from src.request import get_website
from src.scraping_movie import scraping_movie

url_domain = "https://www.imdb.com"
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html_content = get_website(url)


soup = BeautifulSoup(html_content, "html.parser")
movies_container = soup.find_all("li")

data = []

for movie in movies_container[36:286]:
    link_movie = movie.a["href"]

    data.append(scraping_movie(url_domain + link_movie))

print(data)
