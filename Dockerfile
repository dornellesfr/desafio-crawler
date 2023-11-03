FROM python:3.11-buster

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y wget && apt-get install -y wkhtmltopdf

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "./app.py"]
