from django.db import models

# Create your models here.
class Producto(models.Model):
    producto_nombre = models.CharField(max_length=200)
    producto_descripcion = models.TextField()
    producto_ingreso = models.DateField("fecha de ingreso")
    producto_salida = models.DateField("fecha de salida")
    producto_cliente = models.CharField(max_length=200)
    

    def __str__(self):
        return self.producto_nombre

