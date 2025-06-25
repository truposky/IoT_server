import os
import sys
import types

# Ensure project modules can be imported and settings are configured
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.modules['secretkey'] = types.SimpleNamespace(secret_key='test')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_server.settings')

import django
from unittest.mock import patch
import asyncio
from channels.testing import WebsocketCommunicator
from channels.layers import channel_layers, InMemoryChannelLayer
from devices.consumers import DeviceConsumer

# Initialise Django
django.setup()

import pytest

@pytest.mark.asyncio
async def test_websocket_toggle_command():
    """The consumer should accept a command and respond."""
    channel_layers.set('default', InMemoryChannelLayer())
    communicator = WebsocketCommunicator(DeviceConsumer.as_asgi(), "/ws/devices/")
    connected, _ = await communicator.connect()
    assert connected
    with patch('devices.consumers.publish.single') as mock_single:
        await communicator.send_json_to({"command": "TOGGLE"})
        response = await communicator.receive_json_from()
        assert response == {"status": "Comando TOGGLE enviado al Arduino"}
        mock_single.assert_called_once_with(
            "devices/control", "TOGGLE", hostname="localhost", qos=2
        )
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_mqtt_command_forwards_to_consumer():
    """MQTT subscriber forwards incoming messages to WebSocket clients."""
    channel_layers.set('default', InMemoryChannelLayer())
    communicator = WebsocketCommunicator(DeviceConsumer.as_asgi(), "/ws/devices/")
    await communicator.connect()

    class FakeMsg:
        topic = "devices/status"
        payload = b"1"

    class FakeClient:
        def __init__(self):
            self.on_connect = None
            self.on_message = None
        def connect(self, *args, **kwargs):
            if self.on_connect:
                self.on_connect(self, None, None, 0)
        def subscribe(self, *args, **kwargs):
            pass
        def loop_start(self):
            if self.on_message:
                self.on_message(self, None, FakeMsg())
        def loop_stop(self):
            pass

    from devices.management.commands.mqtt_suscriber import Command

    with patch('paho.mqtt.client.Client', return_value=FakeClient()):
        def run_command():
            with patch('time.sleep', side_effect=KeyboardInterrupt):
                Command().handle()

        await asyncio.to_thread(run_command)

    message = await communicator.receive_json_from()
    assert message == {"status": "1"}
    await communicator.disconnect()
