from django.urls import path
from .views import *
app_name="users"
urlpatterns = [
    path("login/",signin,name="login"),
    path("register/",register,name="register"),
]
