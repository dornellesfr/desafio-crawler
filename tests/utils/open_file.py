from bs4 import BeautifulSoup

def open_file(dir_: str):
    with open(dir_, 'r') as f:
        html_movie = f.read()
        soup = BeautifulSoup(html_movie, 'html.parser').text
        return soup
