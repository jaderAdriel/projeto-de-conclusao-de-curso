
from django.shortcuts import render

from django.http import JsonResponse

from django.shortcuts import redirect, render

from Users.forms import RegisterAdminForm, RegisterClientForm, RegisterProfessionalForm

# Create your views here.

def login( request ):
    ...

#--------------------------------------------------------------------

def signup( request ):

    return render(request, 'registration/signup.html')

#--------------------------------------------------------------------

def registerClient( request ):

    if request.method == "POST":

        form = RegisterClientForm( request.POST )

        if form.is_valid():
            form.save()


    context = {
            'form' : RegisterClientForm
        }
    
    return render(request, 'registration/register-client.html', context)

#--------------------------------------------------------------------

def registerAdmin( request ):

    if request.method == "POST":

        form = RegisterAdminForm( request.POST )

        if form.is_valid():
            form.save()


    context = {
            'form' : RegisterAdminForm
        }
    
    return render(request, 'registration/register-admin.html', context)

#--------------------------------------------------------------------

def registerProfessional( request ):
    
    if request.method == "POST":

        form = RegisterProfessionalForm( request.POST )

        if form.is_valid():
            form.save()


    context = {
            'form' : RegisterProfessionalForm
        }
    
    return render(request, 'registration/register-professional.html', context)
