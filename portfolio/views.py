from django.shortcuts import render
from .models import Proyecto

def home(request):
    return render(request, 'index.html')

def project_list(request):
    proyectos = Proyecto.objects.all()  # Recupera todos los proyectos de la base de datos
    return render(request, 'proyectos.html', {'proyectos': proyectos})
