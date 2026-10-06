from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


def logout_view(request):
    """Cierra la sesión y redirige al catálogo."""
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('catalogo:producto_list')


def producto_list(request):
    """Listado público de productos con filtro de categoría y buscador."""
    categoria = request.GET.get('categoria', '')
    query = request.GET.get('q', '')

    productos = Producto.objects.all()

    if categoria:
        productos = productos.filter(categoria=categoria)
    if query:
        productos = productos.filter(nombre__icontains=query)

    context = {
        'productos': productos,
        'categorias': Producto.CATEGORIAS,
        'categoria_seleccionada': categoria,
        'query': query,
    }
    return render(request, 'catalogo/producto_list.html', context)


def producto_detail(request, pk):
    """Detalle de un producto individual."""
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'catalogo/producto_detail.html', {'producto': producto})


@login_required
def producto_create(request):
    """Creación de un nuevo producto (requiere autenticación)."""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" agregado con éxito.')
            return redirect('catalogo:producto_list')
    else:
        form = ProductoForm()

    return render(request, 'catalogo/producto_form.html', {
        'form': form,
        'titulo': 'Agregar Producto'
    })


@login_required
def producto_update(request, pk):
    """Edición de un producto existente (requiere autenticación)."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado con éxito.')
            return redirect('catalogo:producto_detail', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'catalogo/producto_form.html', {
        'form': form,
        'producto': producto,
        'titulo': f'Editar Producto: {producto.nombre}'
    })


@login_required
def producto_delete(request, pk):
    """Eliminación de un producto (requiere autenticación)."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado con éxito.')
        return redirect('catalogo:producto_list')

    return render(request, 'catalogo/producto_confirm_delete.html', {'producto': producto})
