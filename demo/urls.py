from django.shortcuts import render

# Create your views here.


from django.urls import include, path


from . import views
urlpatterns = [
    path('', views.Principal, name='Inicio'),
    path('personas', views.Personas, name='Personas'),
    path('registrar', views.Registrar, name='Registro'),
    path('personas/<int:pk>', views.UnaPersona, name='Persona'),
    path('personas/<int:pk>/eliminar', views.EliminarPersona, name='Eliminar')
    # path('personas', PersonasView.as_view(), name='Personas'),
    # path('personas/<int:pk>', DetalleView.as_view(), name='Persona'),
]
