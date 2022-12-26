from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = UsernameField(widget=forms.TextInput(
        attrs={
            'autocomplete': 'false',
            'placeholder': '',
            'id' : 'email',
            'name' : 'email'
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'false',
            'placeholder': '',
            'id' : 'password',
            'name' : 'password'
        }
    ))