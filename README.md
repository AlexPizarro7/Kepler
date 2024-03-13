# Kepler - Astronomy Software

## Overview
Kepler is a desktop-based application designed for amateur astronomy enthusiasts. Written in Python, Kepler aims to be an informative and educational tool, offering users detailed information about planets, stars, and other celestial objects. 

## Features (Planned/In Development)
- [More features to be added]

## Meet Our Team
-

## Notes for Developers
- This project was developed and tested with a Python Virtual Environment: 3.12.0 ('.venv': venv)
- Command to install a library: `pip install library-name`
- Command to generate or update the requirements.txt file: `pip freeze > requirements.txt`
- Command to install the dependencies of the requirements.txt file: `pip install -r requirements.txt`

## Dockerization
We like Docker because it removes your local machine from the equation. Run everything in their own virtual environments the same way we would deploy to production!

Be sure to install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

To build the architecture to your machine run `docker-compose build`

And to run the application simply run `docker-compose up` add the ` -d` option to run the server in the background.

On first creation be sure to run `docker-compose exec api python manage.py migrate` to build the DB tables.

After first launch you will then have to run the proper django commands to update the DB if you are adding tables esc...

To shutdown the server run `docker-compose down` or use [ctrl-c]

*If you are adding any new python libraries* when working on the BE since you are technically not running on your local env, you are using docker to virtualize, it's important instead of installing to your local you can just include the library into the requirements.txt directly, our build file will run `pip install` so you do not have to. Afterward you must `docker-compose build` for the machine to install the correct libraries.

To Execute any commands inside the venv as if it's local use when the container is running:
`docker-compose exec api {your command}`

You can also use the docker desktop interface to access the terminal visually.

- To populate the DB
`docker-compose exec api python manage.py migrate`

## Access the DB
To view the tables esc... you can open up the console by typing the following in your terminal
`docker-compose exec db psql -U postgres -d postgres`

### Basic Postgres

- `\dt` displays tables

- Normal SQL statements should work as expected


