FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update && apt-get install build-essential -y




COPY . .

CMD [ "python", "main.py"]