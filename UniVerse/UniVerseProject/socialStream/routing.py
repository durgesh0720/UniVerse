from django.urls import path
from .consumers import *

websocket_urlpatterns= [
    path("ws/feeds/",Socialfeeds.as_asgi()),
]