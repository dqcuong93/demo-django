from django import forms
from django.contrib.auth.models import User
import re


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        max_length=100,
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 and password1 == password2:
                return password2
        raise forms.ValidationError('Password is not valid')

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'[!@#$%^&*(),.?":{}|<>;\'\[\]]', username):
            raise forms.ValidationError("Username should not have special character(s)")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        else:
            raise forms.ValidationError('Username already exists')

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
