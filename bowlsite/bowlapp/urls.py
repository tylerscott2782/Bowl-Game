from django.urls import path
from . import views

app_name = "bowlapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("overview", views.overview, name="overview"),
]