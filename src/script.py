from request import get_website
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

html_content = get_website(url)

if html_content:
    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find_all("li")

    for link in links[36:286]:
        print(link.h3)

else:
    print("Fail to get content page.")
