from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

def index(request):
    data = {
        "title":"Главная страница)"
        }
    return render(request, "main/index.html", data)


def about(request):
    return render(request,"main/about.html")