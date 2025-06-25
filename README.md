# IoT Server

This project exposes MQTT commands and websockets using Django Channels.

## Management Command

Use the built-in MQTT subscriber to forward device status messages to WebSocket consumers:

```bash
python manage.py mqtt_subscriber
```

This command connects to the local MQTT broker and broadcasts incoming status updates to WebSocket clients.
