from django import forms
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        json = JSONRenderer().render(fields)


def save(self, commit=True):
    username = self.cleaned_data['username']
    password = self.cleaned_data['password']
    user = User.objects.create_user(username, '', password)
    if commit:
        user.save()
    return user


def check_password(self, commit=True):
    password = self.cleaned_data['password']
    if (len(password) != 0) & (password.isdigit() == False) & (password.isalpha() == False) & (
            password.islower() == False) & (
            password.isupper() == False):
        return True
    else:
        return False
