from django.urls import path
from .views import home, followToggle, signup, results, ChartView, ProfileView, NewChartView, logoutView

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", followToggle, name="login"),
    path("logout/", logoutView, name="logout"),
    path("results/", results, name="results"),
    path("Profile/", ProfileView, name="profile"),
    path("new/", NewChartView, name="new"),
    path("stats/<slug:slug>/", ChartView, name="chart"),
]