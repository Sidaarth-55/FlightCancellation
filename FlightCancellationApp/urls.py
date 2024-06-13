from django.urls import path
from FlightCancellationApp import views

urlpatterns = [
    path("home/", views.upload_form, name="home"),
    path("results/", views.output , name='output-view')
]
