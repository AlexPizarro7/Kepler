from django.test import TestCase
from .views import (
    calculate_celestial_body_rise_utc,
    calculate_celestial_body_set_utc,
    get_coordinates,
    get_timezone,
    convert_utc_to_local
)
from datetime import datetime


class PlanetaryEventsTests(TestCase):
    def test_jupiter_and_saturn_events(self):
        # Define the location and current date
        city = "Moscow"
        country = "Russia"
        today = datetime.today()
        year, month, day = today.year, today.month, today.day

        # Fetch coordinates for Moscow, Russia
        locations = get_coordinates(city, country)
        if not locations:
            print("Failed to retrieve coordinates.")
            return
        # Assuming the first location is correct
        selected_location = locations[0]

        # Get latitude and longitude from the location object
        latitude = selected_location.latitude
        longitude = selected_location.longitude

        # Calculate rise and set times in UTC
        jupiter_rise_utc = calculate_celestial_body_rise_utc(
            "Jupiter Barycenter", year, month, day, latitude, longitude)[0]
        jupiter_set_utc = calculate_celestial_body_set_utc(
            "Jupiter Barycenter", year, month, day, latitude, longitude)[0]
        saturn_rise_utc = calculate_celestial_body_rise_utc(
            "Saturn Barycenter", year, month, day, latitude, longitude)[0]
        saturn_set_utc = calculate_celestial_body_set_utc(
            "Saturn Barycenter", year, month, day, latitude, longitude)[0]

        # Convert UTC to local time
        timezone_name = get_timezone(latitude, longitude)
        jupiter_rise_local = convert_utc_to_local(
            jupiter_rise_utc, timezone_name, year, month, day)
        jupiter_set_local = convert_utc_to_local(
            jupiter_set_utc, timezone_name, year, month, day)
        saturn_rise_local = convert_utc_to_local(
            saturn_rise_utc, timezone_name, year, month, day)
        saturn_set_local = convert_utc_to_local(
            saturn_set_utc, timezone_name, year, month, day)

        # Print results in a simple format
        print(f"Jupiter Rise (Moscow, Local Time): {jupiter_rise_local}")
        print(f"Jupiter Set (Moscow, Local Time): {jupiter_set_local}")
        print(f"Saturn Rise (Moscow, Local Time): {saturn_rise_local}")
        print(f"Saturn Set (Moscow, Local Time): {saturn_set_local}")
