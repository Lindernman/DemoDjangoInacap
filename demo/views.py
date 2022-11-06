import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from demo.models import Persona


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


def UnaPersona(request, pk):
    try:
        persona = Persona.objects.get(id=pk)
    except Persona.DoesNotExist:
        return render(request, 'persona.html', {'error': 'La persona no existe'})

    return render(request, 'persona.html', {'persona': persona})


def EliminarPersona(request, pk):
    Persona.objects.filter(id=pk).delete()
    return redirect('Personas')


# class PersonasView(generic.ListView):
#     template_name = 'personas.html'
#     context_object_name = 'personas'

#     def get_queryset(self):
#         return Persona.objects.values()

# class DetalleView(generic.DetailView):
#     model = Persona
#     template_name = 'persona.html'
