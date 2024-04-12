from django.test import TestCase
from astronomy.views import *
from datetime import datetime
import pytz


class AstronomyTests(TestCase):
    def test_mercury_events_in_nyc(self):
        # Location and date
        city = "New York"
        country = "USA"
        year, month, day = 2024, 4, 10

        # Step 1: Get coordinates and timezone
        locations = get_coordinates(city, country)
        self.assertIsNotNone(locations, "Failed to retrieve coordinates.")
        selected_location = locations[0]
        time_zone_name = get_timezone(
            selected_location.latitude, selected_location.longitude)
        self.assertIsNotNone(time_zone_name, "Failed to retrieve timezone.")

        # Step 2: Calculate Mercury rise, culmination, and set in UTC
        mercury_rise_utc_str = calculate_celestial_body_rise_utc("Mercury", year, month, day,
                                                                 selected_location.latitude, selected_location.longitude)[0]
        mercury_set_utc_str = calculate_celestial_body_set_utc("Mercury", year, month, day,
                                                               selected_location.latitude, selected_location.longitude)[0]
        mercury_culmination_utc_str = calculate_meridian_transit("Mercury", selected_location.latitude,
                                                                 selected_location.longitude, year, month, day)

        # Parse the UTC strings to datetime
        mercury_rise_utc = datetime.fromisoformat(
            mercury_rise_utc_str).replace(tzinfo=pytz.utc)
        mercury_set_utc = datetime.fromisoformat(
            mercury_set_utc_str).replace(tzinfo=pytz.utc)
        mercury_culmination_utc = datetime.fromisoformat(
            mercury_culmination_utc_str).replace(tzinfo=pytz.utc)

        # Step 4: Convert all times to local time
        mercury_rise_local = convert_utc_to_local(
            mercury_rise_utc, time_zone_name, year, month, day)
        mercury_set_local = convert_utc_to_local(
            mercury_set_utc, time_zone_name, year, month, day)
        mercury_culmination_local = convert_utc_to_local(
            mercury_culmination_utc, time_zone_name, year, month, day)

        # Step 5: Print results
        print(f"Mercury rise in New York on {
              year}-{month:02d}-{day:02d}: {mercury_rise_local}")
        print(f"Mercury set in New York on {
              year}-{month:02d}-{day:02d}: {mercury_set_local}")
        print(f"Mercury culmination in New York on {
              year}-{month:02d}-{day:02d}: {mercury_culmination_local}")

# Note: The format for the datetime in the print statements can be adjusted as needed.
