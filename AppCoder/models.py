from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    pais = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Resena(models.Model):
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
    comentario = models.TextField()
    calificacion = models.IntegerField()

    def __str__(self):
        return f"Reseña de '{self.libro.titulo}' por {self.usuario}"