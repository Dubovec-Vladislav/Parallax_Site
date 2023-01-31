from django.shortcuts import render
from .models import Parallax


def index(request):
    return render(request, "parallax/main.html")

