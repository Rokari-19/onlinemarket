from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'marketplace'

urlpatterns = [
    path('', views.index, name='index'), 
    path('contactus/', views.contact, name='contactus'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name= 'marketplace/login.html' ,authentication_form= LoginForm), name='login')
]