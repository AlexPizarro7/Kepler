from django.test import TestCase
from astronomy.views import *


class AstronomyTests(TestCase):

    def test_mars_rise_and_set_times_in_canberra(self):
        # Location and date
        city = "Canberra"
        country = "Australia"
        year, month, day = 2024, 4, 1  # April 1, 2024

        # Get coordinates
        locations = get_coordinates(city, country)
        self.assertTrue(locations, "Failed to retrieve coordinates.")
        selected_location = locations[0]  # Using the first location

        # Calculate Mars rise and set times in UTC
        mars_rise_utc = calculate_planetrise_utc(
            'Mars', year, month, day, selected_location.latitude, selected_location.longitude)
        mars_set_utc = calculate_planetset_utc(
            'Mars', year, month, day, selected_location.latitude, selected_location.longitude)

        # Convert to local time
        time_zone_name = get_timezone(
            selected_location.latitude, selected_location.longitude)
        self.assertTrue(time_zone_name, "Failed to retrieve timezone.")

        for rise_time in mars_rise_utc:
            mars_rise_local = convert_utc_to_local(
                rise_time, time_zone_name, year, month, day)
            print(f"Mars rise time in {city} on {year}-{month:02d}-{day:02d}: {mars_rise_local.strftime(
                '%Y-%m-%d %I:%M %p')} (local time), {rise_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")

        for set_time in mars_set_utc:
            mars_set_local = convert_utc_to_local(
                set_time, time_zone_name, year, month, day)
            print(f"Mars set time in {city} on {year}-{month:02d}-{day:02d}: {mars_set_local.strftime(
                '%Y-%m-%d %I:%M %p')} (local time), {set_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")

# Note: Run this test to get the rise and set times of Mars for Canberra on April 1, 2024.
