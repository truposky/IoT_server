import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import paho.mqtt.publish as publish

class DeviceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "devices_group"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("command") == "TOGGLE":
            # Publicar el comando en el tópico MQTT
            # Usamos async_to_sync para llamar a la función bloqueante de paho-mqtt
            await self.publicar_mqtt("TOGGLE")
            # Envía una respuesta a la interfaz
            await self.send(text_data=json.dumps({"status": "Comando TOGGLE enviado al Arduino"}))

    async def publicar_mqtt(self, mensaje):
        # Publica el mensaje en el tópico "devices/control"
        publish.single("devices/control", mensaje, hostname="localhost", qos=2)
    async def broadcast_message(self, event):
        # Este método se llamará cuando llegue un mensaje "type": "broadcast_message"
        print("broadcast_message llamado:", event)
        message = event["message"]
        # Opcional: imprime para verificar
        print("Broadcast message recibido:", message)
        # Envía el mensaje a la interfaz
        await self.send(text_data=json.dumps(message))
