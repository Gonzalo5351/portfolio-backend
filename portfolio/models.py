from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)  # Título del proyecto
    description = models.TextField()  # Descripción del proyecto
    technologies = models.CharField(max_length=200)  # Tecnologías usadas
    link = models.URLField(max_length=200)  # Enlace al repositorio o demo
    date = models.DateField()  # Fecha de creación del proyecto

    def __str__(self) -> str:
        return self.title  # Lo que se mostrará cuando veas un Proyecto en texto
