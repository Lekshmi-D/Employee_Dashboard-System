from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='employee'))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
