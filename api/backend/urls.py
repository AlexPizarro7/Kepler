from django.contrib import admin
from django.urls import path
from .views import index
from api.views import astronomy_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('astronomy-data/<str:city>/<str:country>/', astronomy_data, name='astronomy-data'),
]
