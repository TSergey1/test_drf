"""
ASGI config for test_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

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
