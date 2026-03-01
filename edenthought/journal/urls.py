from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name=""),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name="my-login"),
    path("my-logout", views.my_logout, name="my-logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create-thought", views.createThought, name="create-thought"),
    path("my-thought", views.my_thoughts, name="my-thought"),
    path("update-thought/<str:pk>", views.updateThoughts, name="update-thought"),
    path("delete-thought/<str:pk>", views.deleteThought, name="delete-thought"),
]
