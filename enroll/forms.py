from django.core import validators
from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-group', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-group', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control form-group', 'placeholder': 'Enter your password'}),
            'confirm_password': forms.PasswordInput(
                attrs={'class': 'form-control form-group', 'placeholder': 'Confirm your password'}),
        }
