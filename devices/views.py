# devices/views.py

from django.shortcuts import render
from django.http import JsonResponse
import paho.mqtt.publish as publish
def dashboard(request):
    return render(request, 'devices/dashboard.html')
def send_command(request):
    publish.single("devices/control","TOGGLE",qos=2, hostname="localhost")
    return JsonResponse({"status": "Comando TOGGLE enviado con éxito"})
