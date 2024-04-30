# Kepler - Astronomy Software

## Overview
Kepler is a desktop-based application designed for amateur astronomy enthusiasts. Written in Python, Kepler aims to be an informative and educational tool, offering users detailed information about planets, stars, and other celestial objects in the context of a calendar for effective organization and planning. 

## Features
- **Celestial Event Calendar**: View a month-long calendar showing the rise and set times of the sun, moon, and planets (Mercury, Venus, Mars, Jupiter, Saturn) based on a chosen date and location.
- **Visibility Insights**: Determine which celestial bodies will be visible in the night sky on any given night, aiding in the planning of stargazing sessions.
- **Appealing Calendar Interface**: Generate a dynamic web-based calendar interface showing the position of celestial objects relative to your location and time of observation.
- **Location-based Predictions**: Enter any global location to receive accurate predictions of celestial events visible from that spot.
- **Event Notifications**: Set alerts for upcoming celestial events like lunar eclipses

## Meet Our Team
- Alex Pizarro-Solis
- Joshua Duda 
- Andrew Alvarez
- Benjamin Garrett
- Eduardo Mara
- Jackson Baggett

## Python Notes for Developers
- This project was developed and tested with a Python Virtual Environment: 3.12.0 ('.venv': venv)
- Command to install a library: `pip install library-name`
- Command to generate or update the requirements.txt file: `pip freeze > requirements.txt`
- Command to install the dependencies of the requirements.txt file: `pip install -r requirements.txt`

## What To Know About Dockerization
We like Docker because it removes your local machine from the equation. Run everything in their own virtual environments the same way we would deploy to production!

Be sure to install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

To build the architecture to your machine run `docker-compose build`

And to run the application simply run `docker-compose up` add the ` -d` option to run the server in the background.

To view the page navigate to localhost:3000 or 127.0.0.1

On first creation be sure to run `docker-compose exec api python manage.py migrate` to build the DB tables.

After first launch you will then have to run the proper django commands to update the DB if you are adding tables esc...

To shutdown the server run `docker-compose down` or use [ctrl-c]

*If you are adding any new python libraries* when working on the BE since you are technically not running on your local env, you are using docker to virtualize, it's important instead of installing to your local you can just include the library into the requirements.txt directly, our build file will run `pip install` so you do not have to. Afterward you must `docker-compose build` for the machine to install the correct libraries.

To Execute any commands inside the venv as if it's local use when the container is running:
`docker-compose exec api {your command}`

You can also use the docker desktop interface to access the terminal visually.

- To populate the DB
`docker-compose exec api python manage.py migrate`

### Guide On Executing and Testing the Software 
- Make sure you have Docker open in the background

- Build the application/images, adds code onto the virtual machine and components `docker-compose build` basically updates the virtual machine 

- Starts the containers on your machine `docker-compose up -d` database, API, web server. Basically executes the virtual machine. 

- In order to see the complete software with the web interface, go to ` localhost:3000` on your browser.

- In order to test the functions only, do `docker-compose exec api python manage.py test` if doing on command prompt on VS Code. If you are doing it on Docker directly, then do `python manage.py test`

- If you are going to add new libraries, don't do it on the computer, do it on the virtual machine such as under 'Exec' in the Docker app, and be sure to update the requirements.txt file. Make sure it matches the machine matches the local, and it should after running the command. 

- To install library, I updated then built the virtual machine, then I used the exec command prompt in the docker app to use pip install then to update the requirements file. Then I ran to install the requirements on my local command prompt to make sure that's installed locally on my virtual environment tho not necessary

- To close down the servers whenever you are done `docker-compose down`



