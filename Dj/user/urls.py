from django.urls import path

from .views import loginUser, logoutUser, registerUser


app_name = "user"

urlpatterns = [
    path("", loginUser, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", registerUser, name="register"),
]
