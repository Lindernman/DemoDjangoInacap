import random
from django.http import HttpResponse
from django.shortcuts import redirect, render

from demo.models import Persona

# Create your views here.
comunas = ['Puente Alto', 'Santiago', 'Macul',
           'Providencia', 'Maipo', 'Buin', 'Nunork']


def Principal(request):
    return render(request, 'index.html')


def Registrar(request):
    print(request.POST['nombre'])
    Persona.objects.create(nombre=request.POST['nombre'], edad=random.randint(
        18, 99), comuna=random.choice(comunas))
    return redirect('Personas')


def Personas(request):
    personas = Persona.objects.values()
    return render(request, 'personas.html', {'personas': personas})


def UnaPersona(request, id):
    try:
        persona = Persona.objects.get(id=id)
        
    except Persona.DoesNotExist:
        return render(request, 'persona.html', {'error': 'La persona no existe'})

    return render(request, 'persona.html', {'persona': persona})
