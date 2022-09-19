FROM python:3.10.7

RUN apt-get update && apt-get upgrade -y

COPY ./requirements.txt /var/www/requirements.txt

WORKDIR /var/www

RUN pip install -r ./requirements.txt

WORKDIR /var/www/app

EXPOSE 8080

ENV MONGO_USER="root"
ENV MONGO_PASSWORD="example"

CMD uvicorn main:app --host 0.0.0.0 --port 8080 --reload
