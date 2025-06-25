# IoT Server

This project uses Django and Channels for IoT-related communication.

## Configuration

`SECRET_KEY` and `DEBUG` settings are loaded from environment variables. You can manage these variables with [`python-decouple`](https://github.com/henriquebastos/python-decouple) using a `.env` file or export them in your shell.

Example `.env` file:

```
SECRET_KEY=change-me
DEBUG=True
```

Install **python-decouple** and create a `.env` file, or simply `export` the variables in your shell:

```bash
export SECRET_KEY=change-me
export DEBUG=True
python manage.py runserver
```

Ensure `SECRET_KEY` is set to a secure value and `DEBUG` is `False` in production.
=======
This project exposes MQTT commands and websockets using Django Channels.

## Management Command

Use the built-in MQTT subscriber to forward device status messages to WebSocket consumers:

```bash
python manage.py mqtt_subscriber
```

This command connects to the local MQTT broker and broadcasts incoming status updates to WebSocket clients.
=======
This project is a simple Django application that demonstrates MQTT and WebSocket integration.

## WebSocket configuration

By default the dashboard page builds the WebSocket URL from the host that
served the request. If you need to point clients to a different WebSocket
endpoint (for example when deploying behind a proxy), set the `WEBSOCKET_URL`
setting or environment variable to the absolute URL:

```bash
export WEBSOCKET_URL="wss://example.com/ws/devices/"
```

When defined this value is used instead of the automatically constructed one.

