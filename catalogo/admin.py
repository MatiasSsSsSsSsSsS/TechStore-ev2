from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'estado', 'fecha_creacion']
    list_filter = ('categoria', 'estado', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('precio', 'stock', 'estado')
    ordering = ('-fecha_creacion',)