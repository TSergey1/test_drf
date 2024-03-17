from chat.consumers import ChatConsumer
from django.urls import path

socket_urlpatterns = [
    path('chat/', ChatConsumer.as_asgi()),
]
