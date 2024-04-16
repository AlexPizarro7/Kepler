from django.http import JsonResponse
from datetime import datetime

def index(request):
    return JsonResponse({"message": "Hello, world!"})
