from  django.urls import path

from . import views

urlpatterns = [
    path("signup", views.UserForm, name='signup'),
    path("hola", views.hola_mundo, name='hola')
]