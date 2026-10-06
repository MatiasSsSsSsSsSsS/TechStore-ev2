from django.db import models


class Producto(models.Model):
    CATEGORIAS = [
        ('consolas', 'Consolas de Videojuegos'),
        ('notebooks', 'Notebooks y Computadores'),
        ('componentes', 'Componentes de Hardware'),
        ('perifericos', 'Periféricos y Accesorios'),
    ]

    nombre = models.CharField(max_length=150, verbose_name='Nombre del Producto')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='consolas', verbose_name='Categoría')
    precio = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Precio (CLP)')
    stock = models.IntegerField(default=0, verbose_name='Stock disponible')
    descripcion = models.TextField(verbose_name='Descripción técnica')
    estado = models.BooleanField(default=True, verbose_name='¿Disponible para venta?')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    @property
    def esta_disponible(self):
        return self.estado and self.stock > 0
