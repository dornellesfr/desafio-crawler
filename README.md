# Challenge Beemon Scraper
 Website: [imdb](https://www.imdb.com/chart/top/?ref_=nv_mv_250) and his top 250 movies

## Objetive
This repository is a challenge Beemon

## Libs:
	- Beautifulsoup
	- pytest
	- pdfkit
	- requests

## Necessarie libs:
It is necessary be installed in your pc:

	- docker;
	- docker-compose
## How to install this project and run
Follows this steps to run the app

`git clone git@github.com:dornellesfr/desafio-crawler.git && cd desafio-crawler`

`docker-compose up -d`

Before the container is already up you should get into it

``docker start -ai crawler_challenge``

You'll get into the container so run

``python3 app.py``

It will start to scraping the pages.

You can follow the execution at file scraper.log with logs showing what movie is scraping.
Result going to output file named as output.json and a screenshot gonna show as screenshot.pdf

## To run tests
To run tests you just need run the command:
 ``- python3 -m pytest``
This command will test all unit tests of Movie Class
