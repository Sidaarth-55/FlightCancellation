from django.urls import path
from FlightCancellationApp import views

urlpatterns = [
    path("", views.home, name="home"),
]
