from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from app.models import Record

class CreateUserFroms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget= PasswordInput())



class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [ 'photo','first_name', 'last_name', 'email', 'phone', 'address', 'city', 'provience', 'country' ]


