from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, ThoughForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Thought


def homepage(request):
    return render(request, "journal/index.html")


# User Registration
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created!")
            return redirect("my-login")

    context = {"RegistrationForm": form}
    return render(request, "journal/register.html", context)


# User login
def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"LoginForm": form}
    return render(request, "journal/my-login.html", context)


# User logout
def my_logout(request):
    auth.logout(request)
    return redirect("")


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "journal/dashboard.html")


# Create thought form
@login_required(login_url="my-login")
def createThought(request):
    form = ThoughForm()
    if request.method == "POST":
        form = ThoughForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            return redirect("my-thought")

    context = {"CreateThoughtForm": form}
    return render(request, "journal/create-though.html", context)


# My thought
@login_required(login_url="my-login")
def my_thoughts(request):
    current_user = request.user.id

    thoughts = Thought.objects.all().filter(user=current_user)
    context = {"AllThoughts": thoughts}
    return render(request, "journal/my-thoughts.html", context)
