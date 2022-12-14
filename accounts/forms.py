from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=220, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(max_length=220, label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }


class LoginForm(forms.Form):
    email = forms.CharField(max_length=220, label='Email Address', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Address'
    }))
    password = forms.CharField(max_length=220, label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))