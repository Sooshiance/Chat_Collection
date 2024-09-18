from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from user import views


app_name = "user"

urlpatterns = [
    path("access/token/", views.CustomTokenObtainPairView.as_view(), name='access-token'),

    path('register/account/', views.RegisterUserAPIView.as_view(), name='register-account'),

    path("refresh/token/", TokenRefreshView.as_view(), name='refresh-token'),
]
