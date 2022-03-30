from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {}

    return render(request, 'desktop132.html', context)