
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class support_admin(forms.ModelForm):
    class Meta:
        model = support
        verbose_name = "поддержка"
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'введите название проблемы'}),
            "text": forms.Textarea(attrs={'placeholder': 'опишите свою проблему'}),

        }

class register_user_form(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'введите своё имя'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'введите электронную почту'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'введите пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'подтвердите пароль'}))

    class Meta:
        model = User
        verbose_name = "регистрация пользователей"
        fields = ("username", "email", "password1", "password2")

class login_user_form(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'введите своё имя', 'id': 'id_username_login'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'введите пароль', 'id': 'id_password_login'}))