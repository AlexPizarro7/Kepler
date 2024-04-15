from django.contrib import admin
from django.urls import path
from .views import index, astronomy_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('astronomy-data/', astronomy_data, name='astronomy-data'),
]
