# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_per': no_personas, 'personas': personas})
