from django.shortcuts import render

# Create your views here.


from django.urls import include, path


from demo.views import Personas, Principal, Registrar, UnaPersona

urlpatterns = [

    path('', Principal, name='Inicio'),
    path('personas', Personas, name='Personas'),
    path('personas/<int:id>', UnaPersona, name='Persona'),
    path('registrar', Registrar, name='Registro')
]
