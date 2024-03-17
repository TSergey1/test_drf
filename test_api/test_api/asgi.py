import os

from django.core.asgi import get_asgi_application

import chat.routing as routing
from channels.routing import ProtocolTypeRouter, URLRouter

from test_api.middleware import ChatMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_api.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": ChatMiddleware(URLRouter(routing.socket_urlpatterns)),
})
