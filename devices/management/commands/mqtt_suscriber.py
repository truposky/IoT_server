# devices/management/commands/mqtt_subscriber.py
import time
import json
import paho.mqtt.client as mqtt
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management.base import BaseCommand

MQTT_BROKER = "localhost"  # O la IP donde corre Mosquitto
MQTT_PORT = 1883
MQTT_TOPIC_STATUS = "devices/status"

class Command(BaseCommand):
    help = "Suscribe a mensajes MQTT de estado y los reenvía vía Django Channels"

    def handle(self, *args, **options):
        client = mqtt.Client()

        def on_connect(client, userdata, flags, rc):
            self.stdout.write("Conectado al broker MQTT con código " + str(rc))
            client.subscribe(MQTT_TOPIC_STATUS)

        def on_message(client, userdata, msg):
            payload = msg.payload.decode()
            self.stdout.write(f"Mensaje recibido en {msg.topic}: {payload}")
            # Enviar el mensaje a través de Channels al grupo "devices_group"
            channel_layer = get_channel_layer()
            
            async_to_sync(channel_layer.group_send)(
                "devices_group",
                {
                    "type": "broadcast_message",
                    "message": {"status": payload}  # Se espera "1" o "0"
                }
            )

        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            client.loop_stop()
            self.stdout.write("Desconectado del broker MQTT")
