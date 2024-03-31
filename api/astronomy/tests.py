from django.test import TestCase
from astronomy.views import *


class AstronomyTests(TestCase):

    def test_location_extraction(self):
        # Known location
        city = "New York"
        country = "USA"
        year, month, day = 2024, 6, 21  # Known date

        # Step 1: Get coordinates
        locations = get_coordinates(city, country)
        self.assertIsNotNone(locations)
        self.assertTrue(len(locations) > 0)

        # Assuming the first location is the correct one
        selected_location = locations[0]

        # Step 2: Get timezone
        timezone = get_timezone(
            selected_location.latitude, selected_location.longitude)
        self.assertIsNotNone(timezone)

        # Step 3: Calculate sunset
        sunset_time = calculate_sunset(
            year, month, day, selected_location.latitude, selected_location.longitude)
        self.assertIsNotNone(sunset_time)

        # Print the sunset time
        print(f"Calculated Sunset Time for {city}, {
              country} on {year}-{month}-{day}: {sunset_time}")
