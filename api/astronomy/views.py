import numpy as np
from astropy.time import Time
from astropy.coordinates import get_sun, get_body
from astropy import units as u
from skyfield.api import Topos, Loader
import pytz
from datetime import datetime
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from skyfield import almanac


def get_coordinates(city, country):
    """
    Gets the location objects for a city and country.

    Parameters:
    - city (str): The city's name.
    - country (str): The country's name.

    Returns:
    - list: A list of location objects or None. Each location object contains attributes like latitude,
            longitude, and address. If no matches are found, returns None.
    """
    geolocator = Nominatim(user_agent="AstronomyAppProject")
    locations = geolocator.geocode(
        f"{city}, {country}", exactly_one=False, language='en')
    return locations


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


def calculate_sunset(year, month, day, latitude, longitude):
    """
    Calculates the sunset time for a given location and date.

    ... [rest of your existing parameters and docstring]

    """
    time_zone = get_timezone(latitude, longitude)
    if not time_zone:
        return "Time zone not found."

    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')

    observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)

    # Set time range for the calculation
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    # Use Skyfield's almanac to find sunset time
    f = almanac.sunrise_sunset(eph, observer)
    times, events = almanac.find_discrete(t0, t1, f)
    for t, event in zip(times, events):
        if event == 1:  # Sunset event is typically represented by 1
            sunset_utc = t.utc_datetime()
            local_timezone = pytz.timezone(time_zone)
            sunset_local = sunset_utc.replace(
                tzinfo=pytz.utc).astimezone(local_timezone)
            return sunset_local.strftime('%Y-%m-%d %H:%M:%S')

    return "Sunset time not found."


def moon_phase(year, month, day):
    """Returns the phase of the moon for a given date."""
    date = Time(f"{year}-{month}-{day}")
    moon = get_body("moon", date)
    sun = get_sun(date)
    elongation = sun.separation(moon)
    phase_angle = np.arccos(np.clip(np.cos(elongation), -1, 1)) * u.deg

    return phase_angle
