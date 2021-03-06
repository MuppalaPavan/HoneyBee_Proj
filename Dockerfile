FROM python:3.8
RUN apt-get update
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install -r requirements.txt