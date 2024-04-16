FROM python:3.12-bullseye

ENV PUTHONDONTWRITEBYTECODE 1 # prevent python from writing pyc files to disc
ENV PYTHONBUFFERED = 1 # show stdout and stderr in cmd line

WORKDIR /api

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Copy from the current director of the Dockerfile to the /api in image
COPY . .

CMD gunicorn -b 0.0.0.0:8000  backend.wsgi:application