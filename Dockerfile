FROM python

WORKDIR /app

COPY . /app/

RUN apt-get update && apt-get install -y wget && apt-get install -y wkhtmltopdf

RUN python3 -m pip install -r requirements.txt

CMD ["/bin/bash"]
