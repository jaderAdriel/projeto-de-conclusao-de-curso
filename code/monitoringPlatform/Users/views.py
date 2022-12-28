
from django.shortcuts import render, redirect

from Users.forms import AdminForm, ClientForm, ProfessionalForm
from Users.models import AuthenticateRequest, User
# Create your views here.


def registerClient( request ):

    if request.method == "POST":

        form = ClientForm( request.POST )

        if form.is_valid():

            new_obj = form.save(commit=False)
            # create hashed password
            new_obj.set_password( form.cleaned_data['password'] )
            new_obj.save()

            return redirect('/users/login/')

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
            new_obj = form.save(commit=False)
            # create hashed password
            new_obj.set_password( form.cleaned_data['password'] )
            new_obj.save()
            return redirect('/users/login/')

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
            new_obj = form.save(commit=False)
            # create hashed password
            new_obj.set_password( form.cleaned_data['password'] )
            # set the user as no authenticated and create a request for authetication
            new_obj.authenticated = False
            new_obj = form.save()
            registerAuthenticateRequest( new_obj )

            return redirect('/users/login/')

    else:
        form = ProfessionalForm()

    context = {
            'form' : form
        }
    
    return render(request, 'registration/professional.html', context)


def registerAuthenticateRequest( instance ):
    request = AuthenticateRequest( professional=instance )
    request.save()