from django.core.exceptions import ValidationError
from django import forms

from Users.models import Admin, Client, Professional



class UserForm( forms.ModelForm ):
    
    password_confirmation = forms.CharField(
        max_length=200, widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        passwordConfirmation = cleaned_data.get("password_confirmation")

        if password != passwordConfirmation:
            err = ValidationError("passwords are not same", code="invalid")
            self.add_error('password_confirmation', err)
        



class AdminForm( UserForm ):

    class Meta:
        model = Admin
        fields = ['name', 'email', 'cpf', 'phone_number', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }


class ClientForm( UserForm ):

    class Meta:
        model = Client
        fields = ['name', 'email', 'cpf', 'phone_number', 'password',]

        widgets = {
            'password': forms.PasswordInput(),
        }



class ProfessionalForm( UserForm ):

    class Meta:
        model = Professional
        exclude = ['last_login', 'authenticated']
        widgets = {
            'password': forms.PasswordInput(),
        }
