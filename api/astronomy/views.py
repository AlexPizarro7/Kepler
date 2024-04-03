import numpy as np
from astropy.time import Time
from astropy.coordinates import get_sun, get_body
from astropy import units as u
from skyfield.api import Topos, Loader
import pytz
from datetime import datetime, timedelta
from timezonefinder import TimezoneFinder
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable, GeocoderServiceError
from geopy.geocoders import Nominatim
from skyfield import almanac


def get_coordinates(city, country, max_retries=3):
    """
    Gets the location objects for a city and country.

    Parameters:
    - city (str): The city's name.
    - country (str): The country's name.
    - max_retries (int): Maximum number of retry attempts for the request.

    Returns:
    - list: A list of location objects or None. Each location object contains attributes like latitude,
            longitude, and address.
    """
    geolocator = Nominatim(user_agent="AstronomyAppProject")
    attempt = 0

    while attempt < max_retries:
        try:
            locations = geolocator.geocode(
                f"{city}, {country}", exactly_one=False, language='en')
            if locations:
                return locations
            else:
                print("No locations found.")
                return None
        except (GeocoderTimedOut, GeocoderUnavailable) as e:
            attempt += 1
            print(f"Geocoder timed out or unavailable, retrying... ({
                  attempt}/{max_retries}). Error: {e}")
        except GeocoderServiceError as e:
            print(f"Geocoder service error: {e}")
            return None

    print("Max retries reached. Returning None.")
    return None


def get_timezone(latitude, longitude):
    """
    Finds the timezone for a given latitude and longitude.

    Parameters:
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - str: Timezone name.
    """
    tz_finder = TimezoneFinder()
    return tz_finder.timezone_at(lat=latitude, lng=longitude)


def calculate_sunset_utc(year, month, day, latitude, longitude):
    """
    Calculate and return the sunset time in UTC for a specified date and location.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    sun = eph['sun']

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    # Extend the time range to the next day to ensure we capture sunset times after midnight UTC
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day, 24)

    # Find sunset times
    t, y = almanac.find_settings(observer, sun, t0, t1)

    for ti, event in zip(t, y):
        sunset_time = ti.utc_datetime()
        # Ensure the sunset time is within the desired day
        if event and sunset_time.date() == datetime(year, month, day).date():
            return sunset_time

    return None


def calculate_astronomical_twilight_utc(year, month, day, latitude, longitude):
    """
    Calculate the start of astronomical twilight for a given date and location.

    Parameters:
    - year (int): Year.
    - month (int): Month.
    - day (int): Day.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - str: Start time of astronomical twilight in UTC as a string.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')

    observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    f = almanac.dark_twilight_day(eph, observer)
    times, events = almanac.find_discrete(t0, t1, f)

    for time, event in zip(times, events):
        # Astronomical twilight start
        if event == 3:
            return time.utc_iso()

    return None


def calculate_planetrise_utc(planet_name, year, month, day, latitude, longitude):
    """
    Calculate and return the planetrise times in UTC for a specified date, location, and planet.

    Parameters:
    - planet_name (str): Name of the planet (e.g., 'Mars', 'Jupiter').
    - year (int): Year of the date.
    - month (int): Month of the date.
    - day (int): Day of the date.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - list: List of planetrise times in UTC.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    planet = eph[planet_name]

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    t, _ = almanac.find_risings(observer, planet, t0, t1)
    return [ti.utc_datetime() for ti in t]


def calculate_planetset_utc(planet_name, year, month, day, latitude, longitude):
    """
    Calculate and return the planetset times in UTC for a specified date, location, and planet.

    Parameters:
    - planet_name (str): Name of the planet (e.g., 'Mars', 'Jupiter').
    - year (int): Year of the date.
    - month (int): Month of the date.
    - day (int): Day of the date.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - list: List of planetset times in UTC.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    planet = eph[planet_name]

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    t, _ = almanac.find_settings(observer, planet, t0, t1)
    return [ti.utc_datetime() for ti in t]


def calculate_planet_culmination(planet_name, latitude, longitude, year, month, day):
    """
    Calculate the time of culmination (transit across the meridian) of a planet 
    for a given location and date.

    Parameters:
    - planet_name (str): The name of the planet (e.g., 'Mars', 'Jupiter').
    - latitude (float): The latitude of the observer.
    - longitude (float): The longitude of the observer.
    - year (int): The year of observation.
    - month (int): The month of observation.
    - day (int): The day of observation.

    Returns:
    - str: The time of culmination in UTC.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')

    # Define the observer with reference to Earth
    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    planet = eph[planet_name]

    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    t, y = almanac.find_transits(observer, planet, t0, t1)

    if len(t):
        return t[0].utc_iso()  # Returns the first transit time in the period
    return None


def calculate_moonrise_utc(year, month, day, latitude, longitude):
    """
    Calculate and return the moonrise times in UTC for a specified date and location.

    Parameters:
    - year (int): Year of the date.
    - month (int): Month of the date.
    - day (int): Day of the date.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - list: List of moonrise times in UTC. Each entry is a datetime object.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    moon = eph['moon']

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    # Set the time range for the specified day
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    # Find moonrise times
    t, y = almanac.find_risings(observer, moon, t0, t1)

    # Filter out the times when the moonrise actually happens
    moonrise_times = [ti.utc_datetime() for ti, event in zip(t, y) if event]
    return moonrise_times


def calculate_moonset_utc(year, month, day, latitude, longitude):
    """
    Calculate and return the moonset times in UTC for a specified date and location.

    Parameters:
    - year (int): Year of the date.
    - month (int): Month of the date.
    - day (int): Day of the date.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - list: List of moonset times in UTC. Each entry is a datetime object.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    moon = eph['moon']

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    # Set the time range for the specified day
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    # Find moonset times
    t, y = almanac.find_settings(observer, moon, t0, t1)

    # Filter out the times when the moonset actually happens
    moonset_times = [ti.utc_datetime() for ti, event in zip(t, y) if event]
    return moonset_times


def convert_utc_to_local(utc_datetime, time_zone_name, year, month, day):
    """
    Convert a UTC datetime to local time in the given time zone, adjusting to match the given year, month, and day.
    """
    local_timezone = pytz.timezone(time_zone_name)
    local_datetime = utc_datetime.replace(
        tzinfo=pytz.utc).astimezone(local_timezone)

    # Ensure the local_datetime matches the given year, month, and day
    if local_datetime.date() != datetime(year, month, day).date():
        # If the local date is earlier, add a day
        local_datetime += timedelta(days=1)

    return local_datetime
