django-admin startproject proyecto
py manage.py startapp demo

0.- Agregar la app al proyecto
    'demo.apps.DemoConfig',



1.-  Agregar la url de la app a base
path('', include('demo.urls'))

1.1.-  Crear urls en la app demo agregar ruta raiz de prueba
    path('', views.Principal, name='Inicio'),

1.2. - Crear la vista inicio o principal para probar

def Principal(request):
    return render(request, 'index.html')

    
2.-  Crear nuestro Modelo


class Persona(models.Model):
    id = models.BigAutoField
    nombre = models.CharField(max_length=100)
    edad = models.SmallIntegerField()
    comuna = models.CharField(max_length=40)

2.1.- migrar el modelo
makemigrations
migrate

3. - Crear plantilla base

4. - Primera ruta a la plantilla 
