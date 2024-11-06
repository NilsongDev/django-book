# inputbook/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    rating = models.PositiveIntegerField()  # Campo para valores positivos
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se establece en el momento de la creación
    fecha_modificacion = models.DateTimeField(auto_now=True)  # Se actualiza en cada modificación

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"



    def __str__(self):
        return self.title
    



    


    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
    permissions = [
        ("development", "Puede realizar tareas de desarrollo"),
        ("scrum_master", "Puede realizar tareas de scrum master"),
    ]





    @property
    def rating_classification(self):
        """Clasificación dinámica de la valoración."""
        if self.rating < 1000:
            return "Baja"
        elif 1000 <= self.rating <= 2500:
            return "Media"
        else:
            return "Alta"
        
