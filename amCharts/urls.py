from django.urls import path
from .views import home, followToggle

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path('login/', followToggle, name="login")
]