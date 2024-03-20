FROM python:3.12-bullseye

ENV PYTHONBUFFERED = 1 # show stdout and stderr in cmd line

WORKDIR /api

COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copy from the current director of the Dockerfile to the /api in image
COPY . .

EXPOSE 8000