from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)  # Título del proyecto
    descripcion = models.TextField()  # Descripción del proyecto
    tecnologias = models.CharField(max_length=200)  # Tecnologías usadas
    enlace = models.URLField(max_length=200)  # Enlace al repositorio o demo
    fecha = models.DateField()  # Fecha de creación del proyecto

    def __str__(self):
        return self.titulo  # Lo que se mostrará cuando veas un Proyecto en texto
