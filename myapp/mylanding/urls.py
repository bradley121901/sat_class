from django.urls import path

from .views import register, filloutform

urlpatterns = [
    path('', register, name='register'),
    path('filloutform', filloutform, name='filloutform')
]