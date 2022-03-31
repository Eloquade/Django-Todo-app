from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'desktop132.html')


def submit(request):
    form = Todo_form
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    if request.method == 'POST':
        form = Todo_form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'desktop2192.html', context)
