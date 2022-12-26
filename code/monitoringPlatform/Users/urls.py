from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/accounts/signup/
    path('signup/', views.signup, name='signup'),
    path( 'login/', views.login, name='login')
]