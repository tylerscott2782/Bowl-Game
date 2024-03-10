from django.urls import path
from . import views

app_name = "bowlapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("profile", views.profile, name="profile"),
]