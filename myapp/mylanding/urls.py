from django.urls import path

from .views import home, register, login

urlpatterns = [
    path('', home, name='home'),
    path('registerpage', register, name='register'),
    path('loginpage', login, name='login')
]