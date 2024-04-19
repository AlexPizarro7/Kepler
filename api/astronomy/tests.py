from django.test import TestCase
from .views import *


class GeocodingLatLongTest(TestCase):
    def test_print_lat_long(self):
        # Test the function with a known city and country
        city = "Molde"
        country = "Norway"
        subdivision = "Møre og Romsdal"
        postal_code = "6400"

        # Fetch the coordinates
        locations = get_coordinates(city, country, subdivision, postal_code)

        # Extract and print the latitude and longitude of the first location found
        if locations:
            first_location = locations[0]  # Get the first location object
            latitude = first_location.latitude
            longitude = first_location.longitude

            print(f"Latitude: {latitude}, Longitude: {longitude}")
        else:
            print("No locations found.")

    def test_lunar_eclipse_on_specific_date(self):
        # This is where you define the date you want to test
        year = 2024
        month = 9
        day = 18

        # Calling the function that checks for lunar eclipses
        check_if_lunar_eclipse(year, month, day)

    def test_twilight_time(self):
        # Location details
        city = "Tyler"
        state = "Texas"
        country = "United States"
        postal_code = "75701"

        # Step 1: Retrieve coordinates
        location_info = get_coordinates(
            city, country, subdivision=state, postal_code=postal_code)
        if location_info is None:
            print("Failed to get coordinates.")
        else:
            # Assume the first result is the most relevant
            latitude = location_info[0].latitude
            longitude = location_info[0].longitude

            # Step 2: Get timezone
            time_zone_name = get_timezone(latitude, longitude)

            # Step 3: Calculate astronomical twilight end time in UTC
            twilight_end_utc = calculate_astronomical_twilight_end_utc(
                2024, 4, 18, latitude, longitude)

            # Step 4: Convert UTC time to local time in 12-hour AM/PM format
            twilight_end_local = convert_utc_to_local(
                twilight_end_utc, time_zone_name, 2024, 4, 18)
            twilight_end_local_time_only = datetime.strptime(
                twilight_end_local, '%Y-%m-%d %H:%M:%S').strftime('%I:%M %p')
            print("Twilight ends at:", twilight_end_local_time_only)
