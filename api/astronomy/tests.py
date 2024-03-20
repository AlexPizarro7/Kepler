from django.test import TestCase
from astronomy.views import moon_phase


class AstronomyTests(TestCase):

    def test_moon_phase(self):
        phase = moon_phase(2024,3,4);
        print(f"The phase of the moon: {phase} ")


