from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/users/register-client/
    path('register-admin/', views.registerAdmin, name='signup'),
    # http://127.0.0.1:8000/users/register-client/
    path('register-client/', views.registerClient, name='registerClient'),
    # http://127.0.0.1:8000/users/register-professional/
    path('register-professional/', views.registerProfessional, name='registerProfessional'),
]