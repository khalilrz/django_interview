from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/images/', consumers.ImageConsumer.as_asgi()),
]
