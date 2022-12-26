
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.shortcuts import redirect, render

from Users.forms import UserLoginForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        ...
        return JsonResponse({'status': '200'})

    else: 
        ...

    return render(request, 'registration/signup.html')
