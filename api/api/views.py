from django.http import JsonResponse
from astronomy.views import *


def location_selector(request, city, country):

    print(request)

    locations = get_coordinates(city, country)

    
    data = {
        "city": locations.city,
        "state": locations.state,
        "country": locations.country,
        "latitude": locations.latitude,
        "longitude": locations.longitude,
    }

    return JsonResponse(data)

def astronomy_data(request,city,country):

    print(request)

    year, month, day = 2024, 4, 10  # example date
    # example coordinates for Tyler, Texas
    latitude, longitude = 32.3513, -95.3011

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
