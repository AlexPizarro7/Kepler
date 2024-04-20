from django.contrib import admin
from django.urls import path
from .views import index
from api.views import location_selector_city, location_selector_state, location_selector_zip

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('location-selector/<str:country>/<str:city>/<str:selected_date>/', location_selector_city, name='location-selector'),
    path('location-selector/<str:country>/<str:city>/<str:state>/<str:selected_date>/', location_selector_state, name='location-selector'),
    path('location-selector/<str:country>/<str:city>/<str:state>/<str:zipcode>/<str:selected_date>/', location_selector_zip, name='location-selector'),


]
