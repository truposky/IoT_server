# import os
# import django
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application

# # 1. Indica a Django dónde están tus settings
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_server.settings')

# # 2. Inicializa Django (opcional, a veces no es necesario llamarlo manualmente)
# django.setup()

# # 3. Importa tu routing DESPUÉS de setdefault
from devices.routing import websocket_urlpatterns

# # 4. Crea la app ASGI para peticiones HTTP normales
# django_asgi_app = get_asgi_application()

# # 5. Combina HTTP y WebSocket
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": URLRouter(websocket_urlpatterns),
# })
import os
from django.core.asgi import get_asgi_application
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_server.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})