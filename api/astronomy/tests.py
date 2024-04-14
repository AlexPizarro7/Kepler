from django.test import TestCase
from astronomy.views import *
import pytz
from datetime import datetime


class AstronomyTests(TestCase):
    def test_celestial_events_in_nyc(self):
        city = "New York"
        country = "USA"
        year, month, day = 2024, 4, 10

        # Retrieve coordinates and timezone
        locations = get_coordinates(city, country)
        self.assertTrue(locations, "Failed to retrieve coordinates.")
        selected_location = locations[0]
        time_zone_name = get_timezone(
            selected_location.latitude, selected_location.longitude)
        self.assertTrue(time_zone_name, "Failed to retrieve timezone.")

        # Calculate celestial times in UTC
        sunrise_utc = calculate_celestial_body_rise_utc("Sun", year, month, day,
                                                        selected_location.latitude, selected_location.longitude)[0]
        sun_culmination_utc = calculate_celestial_body_culmination_utc("Sun", selected_location.latitude,
                                                                       selected_location.longitude, year, month, day)
        sunset_utc = calculate_celestial_body_set_utc("Sun", year, month, day,
                                                      selected_location.latitude, selected_location.longitude)[0]
        twilight_end_utc = calculate_astronomical_twilight_end_utc(year, month, day,
                                                                   selected_location.latitude, selected_location.longitude)

        # Convert UTC to local time directly without needing to parse as datetime
        sunrise_local = convert_utc_to_local(
            sunrise_utc, time_zone_name, year, month, day)
        sun_culmination_local = convert_utc_to_local(
            sun_culmination_utc, time_zone_name, year, month, day)
        sunset_local = convert_utc_to_local(
            sunset_utc, time_zone_name, year, month, day)
        twilight_end_local = convert_utc_to_local(
            twilight_end_utc, time_zone_name, year, month, day)

        # Format times to 12-hour AM/PM format before printing
        sunrise_local_formatted = datetime.strptime(
            sunrise_local, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M %p')
        sun_culmination_local_formatted = datetime.strptime(
            sun_culmination_local, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M %p')
        sunset_local_formatted = datetime.strptime(
            sunset_local, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M %p')
        twilight_end_local_formatted = datetime.strptime(
            twilight_end_local, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M %p')

        # Print the results in a user-friendly 12-hour format
        print(f"Sunrise in New York on {
              year}-{month:02d}-{day:02d}: {sunrise_local_formatted}")
        print(f"Sun culmination in New York on {
              year}-{month:02d}-{day:02d}: {sun_culmination_local_formatted}")
        print(f"Sunset in New York on {
              year}-{month:02d}-{day:02d}: {sunset_local_formatted}")
        print(f"Astronomical Twilight ends in New York on {
              year}-{month:02d}-{day:02d}: {twilight_end_local_formatted}")
