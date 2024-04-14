from django.test import TestCase
from .views import (
    get_coordinates, get_timezone,
    calculate_astronomical_twilight_end_utc, calculate_celestial_body_rise_utc,
    calculate_celestial_body_culmination_utc, calculate_celestial_body_set_utc,
    convert_utc_to_local
)


class AstronomyFunctionTests(TestCase):
    def test_get_coordinates(self):
        result = get_coordinates('New York', 'USA')
        print("Test get_coordinates: Result for New York, USA:", result)
        self.assertIsNotNone(result)

    def test_get_timezone(self):
        result = get_timezone(40.7128, -74.0060)
        print(
            "Test get_timezone: Timezone for latitude 40.7128, longitude -74.0060:", result)
        self.assertEqual(result, 'America/New_York')

    def test_calculate_astronomical_twilight_end_utc(self):
        result = calculate_astronomical_twilight_end_utc(
            2024, 4, 10, 40.7128, -74.0060)
        print("Test calculate_astronomical_twilight_end_utc: Twilight end for 2024-04-10 in NYC:", result)
        self.assertIsInstance(result, str)

    def test_calculate_celestial_body_rise_utc(self):
        result = calculate_celestial_body_rise_utc(
            'Sun', 2024, 4, 10, 40.7128, -74.0060)
        print("Test calculate_celestial_body_rise_utc: Sunrise times for 2024-04-10 in NYC:", result)
        self.assertTrue(len(result) > 0)

    def test_calculate_celestial_body_culmination_utc(self):
        result = calculate_celestial_body_culmination_utc(
            'Sun', 40.7128, -74.0060, 2024, 4, 10)
        print("Test calculate_celestial_body_culmination_utc: Sun culmination time for 2024-04-10 in NYC:", result)
        self.assertIsInstance(result, str)

    def test_calculate_celestial_body_set_utc(self):
        result = calculate_celestial_body_set_utc(
            'Sun', 2024, 4, 10, 40.7128, -74.0060)
        print("Test calculate_celestial_body_set_utc: Sunset times for 2024-04-10 in NYC:", result)
        self.assertTrue(len(result) > 0)

    def test_convert_utc_to_local(self):
        utc_time = '2024-04-10T20:00:00Z'
        result = convert_utc_to_local(
            utc_time, 'America/New_York', 2024, 4, 10)
        print("Test convert_utc_to_local: Local time for 2024-04-10 20:00 UTC in New York:", result)
        self.assertEqual(result, '2024-04-10 16:00:00')
