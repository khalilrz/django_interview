from django.urls import path
from .consumers import ImageConsumer

websocket_urlpatterns = [
    path('ws/images/', ImageConsumer.as_asgi()),
]
