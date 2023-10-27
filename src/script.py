from request import get_website
from bs4 import BeautifulSoup

url_domain = "https://www.imdb.com"
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html_content = get_website(url)


soup = BeautifulSoup(html_content, "html.parser")
movies_container = soup.find_all("li")
top_250_movies_links = []

for movie in movies_container[36:286]:
    link_movie = movie.a["href"]
    top_250_movies_links.append(url_domain + link_movie)

print(top_250_movies_links)
