from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class Todo_form(ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
