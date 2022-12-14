from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import MinimumLengthValidator, validate_password
from django import forms

from Users.models import Admin, Client, Professional

from Users.validators import CpfValidator

class UserForm( forms.ModelForm ):
    
    password_confirmation = forms.CharField(
        max_length=200, widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()

        cpf = cleaned_data.get("cpf")
        password = cleaned_data.get("password")
        passwordConfirmation = cleaned_data.get("password_confirmation")

        if cpf:
            cpf = CpfValidator(cpf)
            if not cpf.is_valid():
                err = ValidationError(cpf.error, code="invalid")
                self.add_error('cpf', err)

        if len(password) < 8:
            self.add_error('password', "Must have at least 8 character long")

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
