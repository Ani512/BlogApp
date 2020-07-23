from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # You can add firstName and LastName here to even add both of those
        fields = ['username', 'email', 'password1', 'password2']
    email = forms.EmailField()
