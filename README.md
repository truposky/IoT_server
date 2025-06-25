# IoT Server

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
