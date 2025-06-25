from django.urls import path
from .consumers import DeviceConsumer

websocket_urlpatterns = [
    path("ws/devices/", DeviceConsumer.as_asgi()),
]
