
from django.urls import path
from robots.views import insert, get_robots_info

robots_urlpatterns = [
    path('api/', insert),
    path('info/', get_robots_info),
]