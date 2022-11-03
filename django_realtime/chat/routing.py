from django.urls import re_path
from django.urls import path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path('ws/chat/(?P<room>\w+)/$', ChatConsumer.as_asgi()),
    path('ws/', ChatConsumer.as_asgi()),
]
