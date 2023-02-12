from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView


def registration(request):
    # form = RegistrationForms
    # data = {
    #     'form':form
    # }

    return render(request, 'registration/registration.html')


