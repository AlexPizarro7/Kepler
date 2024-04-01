from django.test import TestCase
from astronomy.views import *


class AstronomyTests(TestCase):

    def test_sunset_calculation_and_conversion(self):
        # Known location and date
        city = "Kathmandu"
        country = "Nepal"
        year, month, day = 2024, 4, 1

        # Step 1: Get coordinates
        locations = get_coordinates(city, country)
        self.assertIsNotNone(locations, "Failed to retrieve coordinates.")
        self.assertTrue(len(locations) > 0, "No locations found.")

        # Assuming the first location is the correct one
        selected_location = locations[0]

        # Step 2: Calculate sunset in UTC
        sunset_utc = calculate_sunset_utc(
            year, month, day, selected_location.latitude, selected_location.longitude)
        self.assertIsNotNone(sunset_utc, "Failed to calculate sunset in UTC.")
        print(f"Sunset time in UTC for {city}, {country} on {year}-{month:02d}-{day:02d}: "
              f"{sunset_utc.strftime('%H:%M:%S')} UTC")

        # Step 3: Convert UTC sunset time to local time
        time_zone_name = get_timezone(
            selected_location.latitude, selected_location.longitude)
        self.assertIsNotNone(time_zone_name, "Failed to retrieve timezone.")

        sunset_local = convert_utc_to_local(
            sunset_utc, time_zone_name, year, month, day)
        self.assertIsNotNone(
            sunset_local, "Failed to convert UTC time to local time.")
        print(f"Sunset in {city}, {country} on {year}-{month:02d}-{day:02d} "
              f"will be at {sunset_local.strftime('%I:%M %p')} (local time).")
