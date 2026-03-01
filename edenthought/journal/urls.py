from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name=""),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("my-logout", views.my_logout, name="my-logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create-thought", views.createThough, name="create-though"),
]
