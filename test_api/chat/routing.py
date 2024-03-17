from django.urls import path

from chat.consumers import ChatConsumer


socket_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi()),
]
