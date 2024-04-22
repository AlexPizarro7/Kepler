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
        result = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)
        if result is None:
            sunrise_utc = "Setting time not found."
        else:
            sunrise_utc = result[0]
        result = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)
        if result is None:
            sunset_utc = "Setting time not found."
        else:
            sunset_utc = result[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)

        # Mercury rise, set, culmination
        result = calculate_celestial_body_rise_utc("Mercury", year, month, day, latitude, longitude)
        if result is None:
            mercury_rise_utc = "Setting time not found."
        else:
            mercury_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Mercury", year, month, day, latitude, longitude)
        if result is None:
            mercury_set_utc = "Rising time not found."
        else:
            mercury_set_utc = result[0]
        mercury_culmination_utc = calculate_celestial_body_culmination_utc("Mercury", latitude, longitude, year, month, day)

        # Venus rise, set, culmination
        result = calculate_celestial_body_rise_utc("Venus", year, month, day, latitude, longitude)
        if result is None:
            venus_rise_utc = "Setting time not found."
        else:
            venus_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Venus", year, month, day, latitude, longitude)
        if result is None:
            venus_set_utc = "Setting time not found."
        else:
            venus_set_utc = result[0]
        venus_culmination_utc = calculate_celestial_body_culmination_utc("Venus", latitude, longitude, year, month, day)

        # Mars rise, set, culmination
        result = calculate_celestial_body_rise_utc("Mars", year, month, day, latitude, longitude)
        if result is None:
            mars_rise_utc = "Setting time not found."
        else:
            mars_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Mars", year, month, day, latitude, longitude)
        if result is None:
            mars_set_utc = "Setting time not found."
        else:
            mars_set_utc = result[0]
        mars_culmination_utc = calculate_celestial_body_culmination_utc("Mars", latitude, longitude, year, month, day)

         # Neptune rise, set, culmination
        result = calculate_celestial_body_rise_utc("Neptune barycenter", year, month, day, latitude, longitude)
        if result is None:
            neptune_rise_utc = "Setting time not found."
        else:
            neptune_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Neptune barycenter", year, month, day, latitude, longitude)
        if result is None:
            neptune_set_utc = "Setting time not found."
        else:
            neptune_set_utc = result[0]
        neptune_culmination_utc = calculate_celestial_body_culmination_utc("Neptune barycenter", latitude, longitude, year, month, day)
        
        # Jupiter rise, set, culmination
        result = calculate_celestial_body_rise_utc("Jupiter barycenter", year, month, day, latitude, longitude)
        if result is None:
            jupiter_rise_utc = "Setting time not found."
        else:
            jupiter_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Jupiter barycenter", year, month, day, latitude, longitude)
        if result is None:
            jupiter_set_utc = "Setting time not found."
        else:
            jupiter_set_utc = result[0]
        jupiter_culmination_utc = calculate_celestial_body_culmination_utc("Jupiter barycenter", latitude, longitude, year, month, day)

        # Saturn rise, set, culmination
        result = calculate_celestial_body_rise_utc("Saturn barycenter", year, month, day, latitude, longitude)
        if result is None:
            saturn_rise_utc = "Setting time not found."
        else:
            saturn_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Saturn barycenter", year, month, day, latitude, longitude)
        if result is None:
            saturn_set_utc = "Setting time not found."
        else:
            saturn_set_utc = result[0]
        saturn_culmination_utc = calculate_celestial_body_culmination_utc("Saturn barycenter", latitude, longitude, year, month, day)

        timezone = get_timezone(latitude, longitude)

        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "MoonPhase": get_moon_phase_name(year, month, day),
            "LunarEclipse": check_if_lunar_eclipse(year, month, day),
            "Sunrise": convert_utc_to_local(sunrise_utc, timezone, year, month, day),
            "Sunset": convert_utc_to_local(sunset_utc, timezone, year, month, day),
            "SunCulmination": convert_utc_to_local(culmination_utc, timezone, year, month, day),
            "MercuryRise": convert_utc_to_local(mercury_rise_utc, timezone, year, month, day),
            "MercurySet": convert_utc_to_local(mercury_set_utc, timezone, year, month, day),
            "MercuryCulmination": convert_utc_to_local(mercury_culmination_utc, timezone, year, month, day),
            "VenusRise": convert_utc_to_local(venus_rise_utc, timezone, year, month, day),
            "VenusSet": convert_utc_to_local(venus_set_utc, timezone, year, month, day),
            "VenusCulmination": convert_utc_to_local(venus_culmination_utc, timezone, year, month, day),
            "MarsRise": convert_utc_to_local(mars_rise_utc, timezone, year, month, day),
            "MarsSet": convert_utc_to_local(mars_set_utc, timezone, year, month, day),
            "MarsCulmination": convert_utc_to_local(mars_culmination_utc, timezone, year, month, day),
            "JupiterRise": convert_utc_to_local(jupiter_rise_utc, timezone, year, month, day),
            "JupiterSet": convert_utc_to_local(jupiter_set_utc, timezone, year, month, day),
            "JupiterCulmination": convert_utc_to_local(jupiter_culmination_utc, timezone, year, month, day),
            "SaturnRise": convert_utc_to_local(saturn_rise_utc, timezone, year, month, day),
            "SaturnSet": convert_utc_to_local(saturn_set_utc, timezone, year, month, day),
            "SaturnCulmination": convert_utc_to_local(saturn_culmination_utc, timezone, year, month, day),
            "NeptuneRise": convert_utc_to_local(neptune_rise_utc, timezone, year, month, day),
            "NeptuneSet": convert_utc_to_local(neptune_set_utc, timezone, year, month, day),
            "NeptuneCulmination": convert_utc_to_local(neptune_culmination_utc, timezone, year, month, day)
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
        result = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)
        if result is None:
            sunrise_utc = "Setting time not found."
        else:
            sunrise_utc = result[0]
        result = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)
        if result is None:
            sunset_utc = "Setting time not found."
        else:
            sunset_utc = result[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)

        # Mercury rise, set, culmination
        result = calculate_celestial_body_rise_utc("Mercury", year, month, day, latitude, longitude)
        if result is None:
            mercury_rise_utc = "Setting time not found."
        else:
            mercury_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Mercury", year, month, day, latitude, longitude)
        if result is None:
            mercury_set_utc = "Rising time not found."
        else:
            mercury_set_utc = result[0]
        mercury_culmination_utc = calculate_celestial_body_culmination_utc("Mercury", latitude, longitude, year, month, day)

        # Venus rise, set, culmination
        result = calculate_celestial_body_rise_utc("Venus", year, month, day, latitude, longitude)
        if result is None:
            venus_rise_utc = "Setting time not found."
        else:
            venus_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Venus", year, month, day, latitude, longitude)
        if result is None:
            venus_set_utc = "Setting time not found."
        else:
            venus_set_utc = result[0]
        venus_culmination_utc = calculate_celestial_body_culmination_utc("Venus", latitude, longitude, year, month, day)

        # Mars rise, set, culmination
        result = calculate_celestial_body_rise_utc("Mars", year, month, day, latitude, longitude)
        if result is None:
            mars_rise_utc = "Setting time not found."
        else:
            mars_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Mars", year, month, day, latitude, longitude)
        if result is None:
            mars_set_utc = "Setting time not found."
        else:
            mars_set_utc = result[0]
        mars_culmination_utc = calculate_celestial_body_culmination_utc("Mars", latitude, longitude, year, month, day)

         # Neptune rise, set, culmination
        result = calculate_celestial_body_rise_utc("Neptune barycenter", year, month, day, latitude, longitude)
        if result is None:
            neptune_rise_utc = "Setting time not found."
        else:
            neptune_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Neptune barycenter", year, month, day, latitude, longitude)
        if result is None:
            neptune_set_utc = "Setting time not found."
        else:
            neptune_set_utc = result[0]
        neptune_culmination_utc = calculate_celestial_body_culmination_utc("Neptune barycenter", latitude, longitude, year, month, day)
        
        # Jupiter rise, set, culmination
        result = calculate_celestial_body_rise_utc("Jupiter barycenter", year, month, day, latitude, longitude)
        if result is None:
            jupiter_rise_utc = "Setting time not found."
        else:
            jupiter_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Jupiter barycenter", year, month, day, latitude, longitude)
        if result is None:
            jupiter_set_utc = "Setting time not found."
        else:
            jupiter_set_utc = result[0]
        jupiter_culmination_utc = calculate_celestial_body_culmination_utc("Jupiter barycenter", latitude, longitude, year, month, day)

        # Saturn rise, set, culmination
        result = calculate_celestial_body_rise_utc("Saturn barycenter", year, month, day, latitude, longitude)
        if result is None:
            saturn_rise_utc = "Setting time not found."
        else:
            saturn_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Saturn barycenter", year, month, day, latitude, longitude)
        if result is None:
            saturn_set_utc = "Setting time not found."
        else:
            saturn_set_utc = result[0]
        saturn_culmination_utc = calculate_celestial_body_culmination_utc("Saturn barycenter", latitude, longitude, year, month, day)

        timezone = get_timezone(latitude, longitude)

        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "MoonPhase": get_moon_phase_name(year, month, day),
            "LunarEclipse": check_if_lunar_eclipse(year, month, day),
            "Sunrise": convert_utc_to_local(sunrise_utc, timezone, year, month, day),
            "Sunset": convert_utc_to_local(sunset_utc, timezone, year, month, day),
            "SunCulmination": convert_utc_to_local(culmination_utc, timezone, year, month, day),
            "MercuryRise": convert_utc_to_local(mercury_rise_utc, timezone, year, month, day),
            "MercurySet": convert_utc_to_local(mercury_set_utc, timezone, year, month, day),
            "MercuryCulmination": convert_utc_to_local(mercury_culmination_utc, timezone, year, month, day),
            "VenusRise": convert_utc_to_local(venus_rise_utc, timezone, year, month, day),
            "VenusSet": convert_utc_to_local(venus_set_utc, timezone, year, month, day),
            "VenusCulmination": convert_utc_to_local(venus_culmination_utc, timezone, year, month, day),
            "MarsRise": convert_utc_to_local(mars_rise_utc, timezone, year, month, day),
            "MarsSet": convert_utc_to_local(mars_set_utc, timezone, year, month, day),
            "MarsCulmination": convert_utc_to_local(mars_culmination_utc, timezone, year, month, day),
            "JupiterRise": convert_utc_to_local(jupiter_rise_utc, timezone, year, month, day),
            "JupiterSet": convert_utc_to_local(jupiter_set_utc, timezone, year, month, day),
            "JupiterCulmination": convert_utc_to_local(jupiter_culmination_utc, timezone, year, month, day),
            "SaturnRise": convert_utc_to_local(saturn_rise_utc, timezone, year, month, day),
            "SaturnSet": convert_utc_to_local(saturn_set_utc, timezone, year, month, day),
            "SaturnCulmination": convert_utc_to_local(saturn_culmination_utc, timezone, year, month, day),
            "NeptuneRise": convert_utc_to_local(neptune_rise_utc, timezone, year, month, day),
            "NeptuneSet": convert_utc_to_local(neptune_set_utc, timezone, year, month, day),
            "NeptuneCulmination": convert_utc_to_local(neptune_culmination_utc, timezone, year, month, day)
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
        result = calculate_celestial_body_rise_utc("Sun", year, month, day, latitude, longitude)
        if result is None:
            sunrise_utc = "Setting time not found."
        else:
            sunrise_utc = result[0]
        result = calculate_celestial_body_set_utc("Sun", year, month, day, latitude, longitude)
        if result is None:
            sunset_utc = "Setting time not found."
        else:
            sunset_utc = result[0]
        culmination_utc = calculate_celestial_body_culmination_utc("Sun", latitude, longitude, year, month, day)

        # Mercury rise, set, culmination
        result = calculate_celestial_body_rise_utc("Mercury", year, month, day, latitude, longitude)
        if result is None:
            mercury_rise_utc = "Setting time not found."
        else:
            mercury_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Mercury", year, month, day, latitude, longitude)
        if result is None:
            mercury_set_utc = "Rising time not found."
        else:
            mercury_set_utc = result[0]
        mercury_culmination_utc = calculate_celestial_body_culmination_utc("Mercury", latitude, longitude, year, month, day)

        # Venus rise, set, culmination
        result = calculate_celestial_body_rise_utc("Venus", year, month, day, latitude, longitude)
        if result is None:
            venus_rise_utc = "Setting time not found."
        else:
            venus_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Venus", year, month, day, latitude, longitude)
        if result is None:
            venus_set_utc = "Setting time not found."
        else:
            venus_set_utc = result[0]
        venus_culmination_utc = calculate_celestial_body_culmination_utc("Venus", latitude, longitude, year, month, day)

        # Mars rise, set, culmination
        result = calculate_celestial_body_rise_utc("Mars", year, month, day, latitude, longitude)
        if result is None:
            mars_rise_utc = "Setting time not found."
        else:
            mars_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Mars", year, month, day, latitude, longitude)
        if result is None:
            mars_set_utc = "Setting time not found."
        else:
            mars_set_utc = result[0]
        mars_culmination_utc = calculate_celestial_body_culmination_utc("Mars", latitude, longitude, year, month, day)

         # Neptune rise, set, culmination
        result = calculate_celestial_body_rise_utc("Neptune barycenter", year, month, day, latitude, longitude)
        if result is None:
            neptune_rise_utc = "Setting time not found."
        else:
            neptune_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Neptune barycenter", year, month, day, latitude, longitude)
        if result is None:
            neptune_set_utc = "Setting time not found."
        else:
            neptune_set_utc = result[0]
        neptune_culmination_utc = calculate_celestial_body_culmination_utc("Neptune barycenter", latitude, longitude, year, month, day)
        
        # Jupiter rise, set, culmination
        result = calculate_celestial_body_rise_utc("Jupiter barycenter", year, month, day, latitude, longitude)
        if result is None:
            jupiter_rise_utc = "Setting time not found."
        else:
            jupiter_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Jupiter barycenter", year, month, day, latitude, longitude)
        if result is None:
            jupiter_set_utc = "Setting time not found."
        else:
            jupiter_set_utc = result[0]
        jupiter_culmination_utc = calculate_celestial_body_culmination_utc("Jupiter barycenter", latitude, longitude, year, month, day)

        # Saturn rise, set, culmination
        result = calculate_celestial_body_rise_utc("Saturn barycenter", year, month, day, latitude, longitude)
        if result is None:
            saturn_rise_utc = "Setting time not found."
        else:
            saturn_rise_utc = result[0]
        result = calculate_celestial_body_set_utc("Saturn barycenter", year, month, day, latitude, longitude)
        if result is None:
            saturn_set_utc = "Setting time not found."
        else:
            saturn_set_utc = result[0]
        saturn_culmination_utc = calculate_celestial_body_culmination_utc("Saturn barycenter", latitude, longitude, year, month, day)

        timezone = get_timezone(latitude, longitude)

        location = {
            "Latitude": latitude,
            "Longitude": longitude,
            "MoonPhase": get_moon_phase_name(year, month, day),
            "LunarEclipse": check_if_lunar_eclipse(year, month, day),
            "Sunrise": convert_utc_to_local(sunrise_utc, timezone, year, month, day),
            "Sunset": convert_utc_to_local(sunset_utc, timezone, year, month, day),
            "SunCulmination": convert_utc_to_local(culmination_utc, timezone, year, month, day),
            "MercuryRise": convert_utc_to_local(mercury_rise_utc, timezone, year, month, day),
            "MercurySet": convert_utc_to_local(mercury_set_utc, timezone, year, month, day),
            "MercuryCulmination": convert_utc_to_local(mercury_culmination_utc, timezone, year, month, day),
            "VenusRise": convert_utc_to_local(venus_rise_utc, timezone, year, month, day),
            "VenusSet": convert_utc_to_local(venus_set_utc, timezone, year, month, day),
            "VenusCulmination": convert_utc_to_local(venus_culmination_utc, timezone, year, month, day),
            "MarsRise": convert_utc_to_local(mars_rise_utc, timezone, year, month, day),
            "MarsSet": convert_utc_to_local(mars_set_utc, timezone, year, month, day),
            "MarsCulmination": convert_utc_to_local(mars_culmination_utc, timezone, year, month, day),
            "JupiterRise": convert_utc_to_local(jupiter_rise_utc, timezone, year, month, day),
            "JupiterSet": convert_utc_to_local(jupiter_set_utc, timezone, year, month, day),
            "JupiterCulmination": convert_utc_to_local(jupiter_culmination_utc, timezone, year, month, day),
            "SaturnRise": convert_utc_to_local(saturn_rise_utc, timezone, year, month, day),
            "SaturnSet": convert_utc_to_local(saturn_set_utc, timezone, year, month, day),
            "SaturnCulmination": convert_utc_to_local(saturn_culmination_utc, timezone, year, month, day),
            "NeptuneRise": convert_utc_to_local(neptune_rise_utc, timezone, year, month, day),
            "NeptuneSet": convert_utc_to_local(neptune_set_utc, timezone, year, month, day),
            "NeptuneCulmination": convert_utc_to_local(neptune_culmination_utc, timezone, year, month, day)
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