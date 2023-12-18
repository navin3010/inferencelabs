from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        # is_staff = True
        fields = ["first_name", "last_name","username","email", "password"] 