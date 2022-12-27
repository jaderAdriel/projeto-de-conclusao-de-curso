from django.forms import ModelForm


from Users.models import Admin, Client, Professional

class RegisterAdminForm(ModelForm):

    class Meta:
        model = Admin
        exclude = ['last_login'] 


class RegisterClientForm(ModelForm):

    class Meta:
        model = Client
        exclude = ['last_login'] 


class RegisterProfessionalForm(ModelForm):

    class Meta:
        model = Professional
        exclude = ['last_login'] 
