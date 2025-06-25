# devices/views.py

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

import paho.mqtt.publish as publish


def dashboard(request):
    """Render the IoT dashboard with the WebSocket URL in context."""
    websocket_url = getattr(settings, "WEBSOCKET_URL", None)
    if not websocket_url:
        scheme = "wss" if request.is_secure() else "ws"
        websocket_url = f"{scheme}://{request.get_host()}/ws/devices/"

    context = {
        "websocket_url": websocket_url,
    }
    return render(request, "devices/dashboard.html", context)


def send_command(request):
    publish.single("devices/control", "TOGGLE", qos=2, hostname="localhost")
    return JsonResponse({"status": "Comando TOGGLE enviado con éxito"})
