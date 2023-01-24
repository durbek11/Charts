from django.urls import path
from .views import home, followToggle, signup

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path('login/', followToggle, name="login")
]