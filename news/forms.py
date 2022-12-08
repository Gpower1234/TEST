from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField(max_length=50)
    lastName = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "email", "firstName", "lastName", "password1", "password2"]

'''class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='passowrd', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

        def clean(self):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.validationError('invalid login details')'''