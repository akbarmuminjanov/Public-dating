from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

        Profile.objects.create(user=user)
        return redirect("login")
    else:
        form = UserCreationForm()
        return render(request, "users/register.html", {"form":form})
        