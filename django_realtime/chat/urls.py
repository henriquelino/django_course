from django.urls import path
from .views import IndexView, RoomView, room

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('chat/<str:room_name>/', RoomView.as_view(), name='room'),
    path('chat/<str:room_name>/', room, name='room'),
]
