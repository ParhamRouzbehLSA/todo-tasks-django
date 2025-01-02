from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # فیلد ایمیل

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # فیلدهای فرم