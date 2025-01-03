from django.urls import path

from .views import home, allHall, chatPage, createRoom


app_name = "chat"

urlpatterns = [
    path("", home, name="home"),
    path("halls/", allHall, name="halls"),
    path("chat/<int:pk>/", chatPage, name="room"),
    path("create/room/", createRoom, name="create-room"),
]
