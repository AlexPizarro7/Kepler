from django.http import JsonResponse
from astronomy.views import *


def location_selector_city(request, country, city, selected_date):

    print(request)

    locations = get_coordinates(city, country)

    # Extract and print the latitude and longitude of the first location found
    if locations:
        first_location = locations[0]  # Get the first location object
        latitude = first_location.latitude
        longitude = first_location.longitude

        date = selected_date.split("-")
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])

        # Sunrise, sunsetm culimination, twilight end
        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)[0]
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude)

        # Moonrise, moonset, moon culmination
        moonrise_utc = calculate_celestial_body_rise_utc("Moon", year, month, day, latitude, longitude)[0]
        moonset_utc = calculate_celestial_body_set_utc("Moon", year, month, day, latitude, longitude)[0]
        moon_culmination_utc = calculate_celestial_body_culmination_utc("Moon", latitude, longitude, year, month, day)

        # Mercury rise, set, culmination
        mercury_rise_utc = calculate_celestial_body_rise_utc("Mercury", year, month, day, latitude, longitude)[0]
        mercury_set_utc = calculate_celestial_body_set_utc("Mercury", year, month, day, latitude, longitude)[0]
        mercury_culmination_utc = calculate_celestial_body_culmination_utc("Mercury", latitude, longitude, year, month, day)

        # Venus rise, set, culmination
        venus_rise_utc = calculate_celestial_body_rise_utc("Venus", year, month, day, latitude, longitude)[0]
        venus_set_utc = calculate_celestial_body_set_utc("Venus", year, month, day, latitude, longitude)[0]
        venus_culmination_utc = calculate_celestial_body_culmination_utc("Venus", latitude, longitude, year, month, day)

        # Mars rise, set, culmination
        mars_rise_utc = calculate_celestial_body_rise_utc("Mars", year, month, day, latitude, longitude)[0]
        mars_set_utc = calculate_celestial_body_set_utc("Mars", year, month, day, latitude, longitude)[0]
        mars_culmination_utc = calculate_celestial_body_culmination_utc("Mars", latitude, longitude, year, month, day)

        # Jupiter rise, set, culmination
        # jupiter_rise_utc = calculate_celestial_body_rise_utc("5 JUPITER BARYCENTER", year, month, day, latitude, longitude)[0]
        # jupiter_set_utc = calculate_celestial_body_set_utc("5 JUPITER BARYCENTER", year, month, day, latitude, longitude)[0]
        # jupiter_culmination_utc = calculate_celestial_body_culmination_utc("5 JUPITER BARYCENTERr", latitude, longitude, year, month, day)

        # Saturn rise, set, culmination
        # saturn_rise_utc = calculate_celestial_body_rise_utc("Saturn", year, month, day, latitude, longitude)[0]
        # saturn_set_utc = calculate_celestial_body_set_utc("Saturn", year, month, day, latitude, longitude)[0]
        # saturn_culmination_utc = calculate_celestial_body_culmination_utc("Saturn", latitude, longitude, year, month, day)
        
        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Sunrise": sunrise_utc,
            "Sunset": sunset_utc,
            "SunCulmination": culmination_utc,
            "SunTwilightEnd": twilight_end_utc,
            "Moonrise": moonrise_utc,
            "Moonset": moonset_utc,
            "MoonCulmination": moon_culmination_utc,
            "MercuryRise": mercury_rise_utc,
            "MercurySet": mercury_set_utc,
            "MercuryCulmination": mercury_culmination_utc,
            "VenusRise": venus_rise_utc,
            "VenusSet": venus_set_utc,
            "VenusCulmination": venus_culmination_utc,
            "MarsRise": mars_rise_utc,
            "MarsSet": mars_set_utc,
            "MarsCulmination": mars_culmination_utc,
            # "JupiterRise": jupiter_rise_utc,
            # "JupiterSet": jupiter_set_utc,
            # "JupiterCulmination": jupiter_culmination_utc,
            # "SaturnRise": saturn_rise_utc,
            # "SaturnSet": saturn_set_utc,
            # "SaturnCulmination": saturn_culmination_utc
        }
    else:
        location = {
            "Error": "No locations found."
        }

    return JsonResponse(location)

def location_selector_state(request, country, city, state, selected_date):
    print(request)

    locations = get_coordinates(city, country, state)

    # Extract and print the latitude and longitude of the first location found
    if locations:
        first_location = locations[0]  # Get the first location object
        latitude = first_location.latitude
        longitude = first_location.longitude

        date = selected_date.split("-")
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])

        # Sunrise, sunsetm culimination, twilight end
        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)[0]
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude)

        # Moonrise, moonset, moon culmination
        moonrise_utc = calculate_celestial_body_rise_utc("Moon", year, month, day, latitude, longitude)[0]
        moonset_utc = calculate_celestial_body_set_utc("Moon", year, month, day, latitude, longitude)[0]
        moon_culmination_utc = calculate_celestial_body_culmination_utc("Moon", latitude, longitude, year, month, day)

        # Mercury rise, set, culmination
        mercury_rise_utc = calculate_celestial_body_rise_utc("Mercury", year, month, day, latitude, longitude)[0]
        mercury_set_utc = calculate_celestial_body_set_utc("Mercury", year, month, day, latitude, longitude)[0]
        mercury_culmination_utc = calculate_celestial_body_culmination_utc("Mercury", latitude, longitude, year, month, day)

        # Venus rise, set, culmination
        venus_rise_utc = calculate_celestial_body_rise_utc("Venus", year, month, day, latitude, longitude)[0]
        venus_set_utc = calculate_celestial_body_set_utc("Venus", year, month, day, latitude, longitude)[0]
        venus_culmination_utc = calculate_celestial_body_culmination_utc("Venus", latitude, longitude, year, month, day)

        # Mars rise, set, culmination
        mars_rise_utc = calculate_celestial_body_rise_utc("Mars", year, month, day, latitude, longitude)[0]
        mars_set_utc = calculate_celestial_body_set_utc("Mars", year, month, day, latitude, longitude)[0]
        mars_culmination_utc = calculate_celestial_body_culmination_utc("Mars", latitude, longitude, year, month, day)

        # Jupiter rise, set, culmination
        # jupiter_rise_utc = calculate_celestial_body_rise_utc("5 JUPITER BARYCENTER", year, month, day, latitude, longitude)[0]
        # jupiter_set_utc = calculate_celestial_body_set_utc("5 JUPITER BARYCENTER", year, month, day, latitude, longitude)[0]
        # jupiter_culmination_utc = calculate_celestial_body_culmination_utc("5 JUPITER BARYCENTER", latitude, longitude, year, month, day)

        # Saturn rise, set, culmination
        # saturn_rise_utc = calculate_celestial_body_rise_utc("Saturn", year, month, day, latitude, longitude)[0]
        # saturn_set_utc = calculate_celestial_body_set_utc("Saturn", year, month, day, latitude, longitude)[0]
        # saturn_culmination_utc = calculate_celestial_body_culmination_utc("Saturn", latitude, longitude, year, month, day)
        
        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Sunrise": sunrise_utc,
            "Sunset": sunset_utc,
            "SunCulmination": culmination_utc,
            "SunTwilightEnd": twilight_end_utc,
            "Moonrise": moonrise_utc,
            "Moonset": moonset_utc,
            "MoonCulmination": moon_culmination_utc,
            "MercuryRise": mercury_rise_utc,
            "MercurySet": mercury_set_utc,
            "MercuryCulmination": mercury_culmination_utc,
            "VenusRise": venus_rise_utc,
            "VenusSet": venus_set_utc,
            "VenusCulmination": venus_culmination_utc,
            "MarsRise": mars_rise_utc,
            "MarsSet": mars_set_utc,
            "MarsCulmination": mars_culmination_utc,
            # "JupiterRise": jupiter_rise_utc,
            # "JupiterSet": jupiter_set_utc,
            # "JupiterCulmination": jupiter_culmination_utc,
            # "SaturnRise": saturn_rise_utc,
            # "SaturnSet": saturn_set_utc,
            # "SaturnCulmination": saturn_culmination_utc
        }
    else:
        location = {
            "Error": "No locations found."
        }

    return JsonResponse(location)

def location_selector_zip(request, country, city, state, zipcode, selected_date):
    print(request)

    locations = get_coordinates(city, country, state, zipcode)

    # Extract and print the latitude and longitude of the first location found
    if locations:
        first_location = locations[0]  # Get the first location object
        latitude = first_location.latitude
        longitude = first_location.longitude

        date = selected_date.split("-")
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])

        # Sunrise, sunsetm culimination, twilight end
        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)[0]
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude)

        # Moonrise, moonset, moon culmination
        moonrise_utc = calculate_celestial_body_rise_utc("Moon", year, month, day, latitude, longitude)[0]
        moonset_utc = calculate_celestial_body_set_utc("Moon", year, month, day, latitude, longitude)[0]
        moon_culmination_utc = calculate_celestial_body_culmination_utc("Moon", latitude, longitude, year, month, day)

        # Mercury rise, set, culmination
        mercury_rise_utc = calculate_celestial_body_rise_utc("Mercury", year, month, day, latitude, longitude)[0]
        mercury_set_utc = calculate_celestial_body_set_utc("Mercury", year, month, day, latitude, longitude)[0]
        mercury_culmination_utc = calculate_celestial_body_culmination_utc("Mercury", latitude, longitude, year, month, day)

        # Venus rise, set, culmination
        venus_rise_utc = calculate_celestial_body_rise_utc("Venus", year, month, day, latitude, longitude)[0]
        venus_set_utc = calculate_celestial_body_set_utc("Venus", year, month, day, latitude, longitude)[0]
        venus_culmination_utc = calculate_celestial_body_culmination_utc("Venus", latitude, longitude, year, month, day)

        # Mars rise, set, culmination
        mars_rise_utc = calculate_celestial_body_rise_utc("Mars", year, month, day, latitude, longitude)[0]
        mars_set_utc = calculate_celestial_body_set_utc("Mars", year, month, day, latitude, longitude)[0]
        mars_culmination_utc = calculate_celestial_body_culmination_utc("Mars", latitude, longitude, year, month, day)

        # Jupiter rise, set, culmination
        # jupiter_rise_utc = calculate_celestial_body_rise_utc("5 JUPITER BARYCENTER", year, month, day, latitude, longitude)[0]
        # jupiter_set_utc = calculate_celestial_body_set_utc("5 JUPITER BARYCENTER", year, month, day, latitude, longitude)[0]
        # jupiter_culmination_utc = calculate_celestial_body_culmination_utc("5 JUPITER BARYCENTER", latitude, longitude, year, month, day)

        # Saturn rise, set, culmination
        # saturn_rise_utc = calculate_celestial_body_rise_utc("Saturn", year, month, day, latitude, longitude)[0]
        # saturn_set_utc = calculate_celestial_body_set_utc("Saturn", year, month, day, latitude, longitude)[0]
        # saturn_culmination_utc = calculate_celestial_body_culmination_utc("Saturn", latitude, longitude, year, month, day)
        
        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Sunrise": sunrise_utc,
            "Sunset": sunset_utc,
            "SunCulmination": culmination_utc,
            "SunTwilightEnd": twilight_end_utc,
            "Moonrise": moonrise_utc,
            "Moonset": moonset_utc,
            "MoonCulmination": moon_culmination_utc,
            "MercuryRise": mercury_rise_utc,
            "MercurySet": mercury_set_utc,
            "MercuryCulmination": mercury_culmination_utc,
            "VenusRise": venus_rise_utc,
            "VenusSet": venus_set_utc,
            "VenusCulmination": venus_culmination_utc,
            "MarsRise": mars_rise_utc,
            "MarsSet": mars_set_utc,
            "MarsCulmination": mars_culmination_utc,
            # "JupiterRise": jupiter_rise_utc,
            # "JupiterSet": jupiter_set_utc,
            # "JupiterCulmination": jupiter_culmination_utc,
            # "SaturnRise": saturn_rise_utc,
            # "SaturnSet": saturn_set_utc,
            # "SaturnCulmination": saturn_culmination_utc
        }
    else:
        location = {
            "Error": "No locations found."
        }

    return JsonResponse(location)

def update_date(request, lat, long, selected_date):
    print(request)

    year, month, day = selected_date.split("-")

    year = int(year)
    month = int(month)
    day = int(day)

    # example coordinates for Tyler, Texas
    latitude, longitude = lat, long

    sunrise_utc = calculate_celestial_body_rise_utc(
        "Sun", year, month, day, latitude, longitude)[0]
    sunset_utc = calculate_celestial_body_set_utc(
        "Sun", year, month, day, latitude, longitude)[0]
    culmination_utc = calculate_celestial_body_culmination_utc(
        "Sun", latitude, longitude, year, month, day)
    twilight_end_utc = calculate_astronomical_twilight_end_utc(
        year, month, day, latitude, longitude)

    data = {
        "sunrise": sunrise_utc,
        "sunset": sunset_utc,
        "culmination": culmination_utc,
        "twilight_end": twilight_end_utc
    }

    return JsonResponse(data)