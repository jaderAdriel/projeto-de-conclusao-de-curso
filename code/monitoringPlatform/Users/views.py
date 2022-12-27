
from django.shortcuts import render

from Users.forms import AdminForm, ClientForm, ProfessionalForm
from Users.models import AuthenticateRequest
# Create your views here.


def registerClient( request ):

    if request.method == "POST":

        form = ClientForm( request.POST )

        if form.is_valid():
            form.save()

    else:
        form = ClientForm()

    context = {
            'form' : form
        }
    
    return render(request, 'registration/client.html', context)

#--------------------------------------------------------------------

def registerAdmin( request ):

    if request.method == "POST":

        form = AdminForm( request.POST )

        if form.is_valid():
            form.save()

    else:
        form = AdminForm()

    context = {
            'form' : form
        }
    
    return render(request, 'registration/admin.html', context)

#--------------------------------------------------------------------

def registerProfessional( request ):
    
    if request.method == "POST":

        form = ProfessionalForm( request.POST )

        if form.is_valid():
            form.save(commit=False)
            form.authenticated = False
            new = form.save()
            registerAuthenticateRequest( new )

    else:
        form = ProfessionalForm()

    context = {
            'form' : form
        }
    
    return render(request, 'registration/professional.html', context)


def registerAuthenticateRequest( instance ):
    request = AuthenticateRequest( professional=instance )
    request.save()