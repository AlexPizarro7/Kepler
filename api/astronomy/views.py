from skyfield.api import Loader
from datetime import datetime
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
from skyfield import almanac, eclipselib
from skyfield.almanac import find_discrete


def get_coordinates(city, country, subdivision=None, postal_code=None, max_retries=3):
    """
    Gets the location objects for a detailed place using city, subdivision, postal code, and country.

    Parameters:
    - city (str): The city's name.
    - country (str): The country's name.
    - subdivision (str): The state, province, or other subdivision. Optional.
    - postal_code (str): The postal or ZIP code. Optional.
    - max_retries (int): Maximum number of retry attempts for the request.

    Returns:
    - list: A list of location objects or None. Each location object contains attributes like latitude,
            longitude, and address.
    """
    geolocator = Nominatim(user_agent="AstronomyAppProject")
    attempt = 0

    # Construct the location query based on the presence of optional parameters
    location_components = [city]
    if subdivision:
        location_components.append(subdivision)
    if postal_code:
        location_components.append(postal_code)
    location_components.append(country)

    location_query = ", ".join(filter(None, location_components))

    while attempt < max_retries:
        try:
            locations = geolocator.geocode(
                location_query, exactly_one=False, language='en')
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


def calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude):
    """
    Calculate the end of astronomical twilight for a given date and location.

    Parameters:
    - year (int): Year.
    - month (int): Month.
    - day (int): Day.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - str: End time of astronomical twilight in UTC as a string.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')

    observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    f = almanac.dark_twilight_day(eph, observer)
    times, events = almanac.find_discrete(t0, t1, f)

    previous_event = f(t0).item()
    for time, event in zip(times, events):
        if previous_event == 2 and event == 1:
            # End of astronomical twilight (transition to full night)
            return time.utc_iso()
        previous_event = event

    return "Twilight end not found."


def calculate_celestial_body_rise_utc(body_name, year, month, day, latitude, longitude):
    """
    Calculate and return the rise times in UTC for a specified date, location, and celestial body, as strings.

    Parameters:
    - body_name (str): Name of the celestial body (e.g., 'Sun', 'Moon', 'Mars', 'Jupiter').
    - year (int): Year of the date.
    - month (int): Month of the date.
    - day (int): Day of the date.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - list: List of rise times in UTC as ISO formatted strings.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    body = eph[body_name]

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    t, _ = almanac.find_risings(observer, body, t0, t1)
    return [ti.utc_iso() for ti in t]


def calculate_celestial_body_culmination_utc(planet_name, latitude, longitude, year, month, day):
    """
    Calculate the meridian transit (time when the planet is highest in the sky) 
    also known as culmination,for a given location and date, and return it as a string.

    Parameters:
    - planet_name (str): The name of the planet (e.g., 'Mars', 'Jupiter').
    - latitude (float): The latitude of the observer.
    - longitude (float): The longitude of the observer.
    - year (int): The year of observation.
    - month (int): The month of observation.
    - day (int): The day of observation.

    Returns:
    - str: The time of the meridian transit (culmination) in UTC as a string.
    """
    from skyfield import almanac

    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')

    observer = Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    planet = eph[planet_name]

    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    f = almanac.meridian_transits(eph, planet, observer)
    times, events = almanac.find_discrete(t0, t1, f)

    for t, event in zip(times, events):
        if event == 1:  # 1 indicates meridian transit
            return t.utc_iso()

    return "Meridian transit not found."


def calculate_celestial_body_set_utc(body_name, year, month, day, latitude, longitude):
    """
    Calculate and return the setting times in UTC for a specified date, location, and celestial body, as strings.

    Parameters:
    - body_name (str): Name of the celestial body (e.g., 'Sun', 'Mars', 'Jupiter').
    - year (int): Year of the date.
    - month (int): Month of the date.
    - day (int): Day of the date.
    - latitude (float): Latitude of the location.
    - longitude (float): Longitude of the location.

    Returns:
    - list: List of setting times in UTC as ISO formatted strings.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    body = eph[body_name]

    observer = eph['earth'] + \
        Topos(latitude_degrees=latitude, longitude_degrees=longitude)
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    t, _ = almanac.find_settings(observer, body, t0, t1)
    return [ti.utc_iso() for ti in t]


def convert_utc_to_local(utc_datetime_str, time_zone_name, year, month, day):
    """
    Convert a UTC datetime string to local time in the given time zone, adjusting to match the given year, month, and day.

    Parameters:
    - utc_datetime_str (str): UTC datetime in ISO format to be converted.
    - time_zone_name (str): Timezone name.
    - year (int): Year of the desired local date.
    - month (int): Month of the desired local date.
    - day (int): Day of the desired local date.

    Returns:
    - str: Local time as a string in 'YYYY-MM-DD HH:MM:SS' format, adjusted to match the given year, month, and day.
    """
    # Parse the UTC datetime string into a datetime object
    utc_datetime = datetime.fromisoformat(utc_datetime_str)

    # Convert to the specified timezone
    local_timezone = pytz.timezone(time_zone_name)
    local_datetime = utc_datetime.replace(
        tzinfo=pytz.utc).astimezone(local_timezone)

    # Adjust the date if it does not match
    desired_date = datetime(year, month, day)
    if local_datetime.date() != desired_date.date():
        date_diff = desired_date.date() - local_datetime.date()
        local_datetime += timedelta(days=date_diff.days)

    # Format the datetime object into a string
    return local_datetime.strftime('%Y-%m-%d %H:%M:%S')


def get_moon_phase_name(year, month, day):
    """
    Calculate the detailed Moon's phase name for a given date.

    Parameters:
    - year (int): Year.
    - month (int): Month.
    - day (int): Day.

    Returns:
    - str: Detailed name of the Moon phase.
    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')
    t = ts.utc(year, month, day)
    phase_angle = almanac.moon_phase(eph, t).degrees

    # Normalize the phase angle to be within [0, 360) degrees
    phase_angle = phase_angle % 360

    # Define all Moon phase names based on angle ranges
    if 0 <= phase_angle < 22.5 or 337.5 <= phase_angle < 360:
        phase_name = "New Moon"
    elif 22.5 <= phase_angle < 67.5:
        phase_name = "Waxing Crescent"
    elif 67.5 <= phase_angle < 112.5:
        phase_name = "First Quarter"
    elif 112.5 <= phase_angle < 157.5:
        phase_name = "Waxing Gibbous"
    elif 157.5 <= phase_angle < 202.5:
        phase_name = "Full Moon"
    elif 202.5 <= phase_angle < 247.5:
        phase_name = "Waning Gibbous"
    elif 247.5 <= phase_angle < 292.5:
        phase_name = "Last Quarter"
    elif 292.5 <= phase_angle < 337.5:
        phase_name = "Waning Crescent"

    return phase_name


def check_if_lunar_eclipse(year, month, day):
    """
    Checks for lunar eclipses on a specified date and prints the type if one occurs.

    Parameters:
        year (int): Year to check for an eclipse.
        month (int): Month to check for an eclipse.
        day (int): Day to check for an eclipse.

    Returns:
        None. If an eclipse occurs on the specified date, prints the type of eclipse
        (e.g., 'Total', 'Partial', 'Penumbral'). If no eclipse occurs, prints nothing.

    """
    load = Loader('~/.skyfield-data')
    ts = load.timescale()
    eph = load('de421.bsp')

    # Create a time range around the given date
    t0 = ts.utc(year, month, day)
    t1 = ts.utc(year, month, day + 1)

    # Find lunar eclipses within this range
    t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)

    # If there are any eclipses on this day, print only the type of eclipse
    if len(t) > 0:
        for yi in y:
            # Get the type of eclipse from the dictionary
            eclipse_type = eclipselib.LUNAR_ECLIPSES[yi]
            print(f"There will be a {
                  eclipse_type} Lunar Eclipse on this date.")
