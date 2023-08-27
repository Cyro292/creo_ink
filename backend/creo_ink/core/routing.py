# core/routing.py
from django.urls import re_path, include

websocket_urlpatterns = [
    include('boards.routing'),
]

