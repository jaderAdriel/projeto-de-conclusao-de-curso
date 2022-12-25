from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
def registrarUsuario(request):
    if request.method == "POST":
        ...
    else: 
        ...

      

    return render(request, 'registration/registrar.html')