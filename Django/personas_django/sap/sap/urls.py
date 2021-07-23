from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido
from personas.views import detallePersonas
from personas.views import nuevaPersona
from personas.views import editarPersona
from personas.views import eliminarPersona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('detalle_persona/<int:id>', detallePersonas),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona)
]
