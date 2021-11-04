from django.urls import path
from .views import UserLogin, UserRegister

urlpatterns = [
    path("accounts/", UserRegister.as_view()),
    path("login/", UserLogin.as_view()),
]
