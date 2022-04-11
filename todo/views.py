from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'desktop132.html')


def submit(request):
    form = TodoForm
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        # return redirect('/')
    context = {'form': form}
    return render(request, 'desktop2192.html', context)


def list(request):
    todo = Todo.objects.all()
    context = {'todo': todo}
    return render(request, 'list.html', context)


def updatetodo(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)
    context = {'form': form}
    return render(request, 'update.html', context)
