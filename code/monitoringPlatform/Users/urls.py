from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/users/signup/
    path('signup/', views.signup, name='signup'),
    # http://127.0.0.1:8000/users/login/
]