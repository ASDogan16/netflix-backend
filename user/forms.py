from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.contrib.auth.models import User
from .models import *


class UserLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'})


        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placegolder': 'Profil İsmi'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class': 'form-control'})