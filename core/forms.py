from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'enter your username',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'enter your password',
        'class':'w-full px-6 py-4 rounded-xl'
    }))

class SignUpForm(UserCreationForm):
    model = User
    fields = [
        'username',
        'email',
        'password1',
        'password2',
    ]
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'enter your username',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder':'enter your email',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'enter your password',
        'class':'w-full px-6 py-4 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Repeat your password',
        'class':'w-full px-6 py-4 rounded-xl'
    }))