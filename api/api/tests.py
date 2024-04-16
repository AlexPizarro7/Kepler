from django.test import TestCase
from api.astronomy.views import getCoordinates

# Create your tests here.

def test_location_selector(self):
    city = 'Chicago'
    country = 'USA'
    result = getCoordinates(city, country)
    print(result)