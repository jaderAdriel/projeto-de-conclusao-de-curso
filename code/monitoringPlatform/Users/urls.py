from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/users/signup/
    path('signup/', views.signup, name='signup'),

    path('register-client/', views.registerClient, name='registerClient'),
    
    path('register-professional/', views.registerProfessional, name='register-professional'),
    # http://127.0.0.1:8000/users/login/
    path('login/', views.login, name='login'),
]