from django.urls import path
from .views import moon_phase

urlpatterns = [
    path('/astronomy', moon_phase),
]
