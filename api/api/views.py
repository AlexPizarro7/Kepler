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


        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)[0]
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude)
        
        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Sunrise": sunrise_utc,
            "Sunset": sunset_utc,
            "Culmination": culmination_utc,
            "TwilightEnd": twilight_end_utc
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


        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)[0]
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude)
        
        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Sunrise": sunrise_utc,
            "Sunset": sunset_utc,
            "Culmination": culmination_utc,
            "TwilightEnd": twilight_end_utc
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


        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)[0]
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day, latitude, longitude)
        
        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "Sunrise": sunrise_utc,
            "Sunset": sunset_utc,
            "Culmination": culmination_utc,
            "TwilightEnd": twilight_end_utc
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