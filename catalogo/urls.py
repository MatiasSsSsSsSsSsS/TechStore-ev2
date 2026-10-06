from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # Vistas Públicas
    path('', views.producto_list, name='producto_list'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),

    # Vistas Privadas (CRUD)
    path('producto/nuevo/', views.producto_create, name='producto_create'),
    path('producto/<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('producto/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]
