from django.shortcuts import render, redirect
from .models import Project
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms

def home(request):
    return render(request, 'index.html')

def project_list(request):
    projects = Project.objects.all()  # Recupera todos los proyectos de la base de datos
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name: # We verify that name is not None
            return HttpResponse(f"Thank you {name}, we have received your message.")
        else:
            return HttpResponse("No name provided!")
        # Aquí puedes agregar el procesamiento del mensaje, como enviarlo por correo electrónico
        # o almacenarlo en una base de datos.

    
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def manage_projects(request):
    projects = Proyecto.objects.all()  # Consulta para obtener los proyectos
    return render(request, 'manage_projects.html', {'projects': projects})

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'link', 'date']

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_projects')  # Redirects to project management view 
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})
