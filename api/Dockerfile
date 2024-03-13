FROM python:3.12-bullseye

ENV PYTHONBUFFERED = 1 # show stdout and stderr in cmd line

WORKDIR /api

RUN pip install django django-cors-headers

#Copy from the current director of the Dockerfile to the /api in image
COPY . .

EXPOSE 8000