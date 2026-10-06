from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'stock', 'descripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 350000'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 10'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del producto'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio': 'Precio ($ CLP)',
            'stock': 'Stock Disponible',
            'descripcion': 'Descripción',
            'estado': 'Disponible para la venta',
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0.")
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock
