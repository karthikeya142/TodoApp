from django import forms
from django.shortcuts import redirect, render

from .models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']

