
from django.urls import path
from robots.views import insert

robots_urlpatterns = [
    path('api/', insert),
]