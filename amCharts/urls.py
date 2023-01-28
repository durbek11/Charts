from django.urls import path
from .views import home, followToggle, signup, results, ProfileView

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", followToggle, name="login"),
    path("results/", results, name="results"),
    path("Profile/", ProfileView, name="profile")
]