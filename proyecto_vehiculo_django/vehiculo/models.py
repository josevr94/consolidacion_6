from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Marca(models.Model):
    marca = models.CharField(max_length=200,choices=[
        ('fiat','Fiat'),
        ('Chevrolet','chevrolet'),
        ('Ford','ford'),
        ('Toyota','toyota')
    ],default='Ford')
    
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20,choices=[
        ('Particular','particular'),
        ('Transporte','transporte'),
        ('Carga','carga')
    ],default='Particular')
    
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        permissions = [
            ('visualizar_lista','Puede visualizar la lista de vehiculos')
        ]