from django.contrib import admin
from .models import Marca
# Register your models here.


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('marca','modelo','serial_carroceria','serial_motor','categoria','precio','fecha_creacion','fecha_modificacion')