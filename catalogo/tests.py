from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Producto


class ProductoModelTests(TestCase):
    # Verifica que el nombre del producto se muestre correctamente y que el producto
    # se considere disponible cuando tiene stock y está activo.
    def test_producto_str_y_disponibilidad(self):
        producto = Producto.objects.create(
            nombre='Laptop Gamer',
            categoria='notebooks',
            precio=1200000,
            stock=4,
            descripcion='Laptop para trabajo y gaming.',
            estado=True,
        )

        self.assertEqual(str(producto), 'Laptop Gamer')
        self.assertTrue(producto.esta_disponible)

    # Comprueba que un producto sin stock no se considera disponible para venta.
    def test_producto_no_disponible_si_no_hay_stock(self):
        producto = Producto.objects.create(
            nombre='Teclado',
            categoria='perifericos',
            precio=50000,
            stock=0,
            descripcion='Teclado mecánico.',
            estado=True,
        )

        self.assertFalse(producto.esta_disponible)


class ProductoViewTests(TestCase):
    def setUp(self):
        # Datos base para probar las vistas relacionadas con el catálogo.
        self.producto = Producto.objects.create(
            nombre='Monitor 27',
            categoria='perifericos',
            precio=180000,
            stock=2,
            descripcion='Monitor 27 pulgadas 4K.',
            estado=True,
        )
        self.user = get_user_model().objects.create_user(
            username='tester',
            password='123456',
        )

    # Verifica que la vista pública del catálogo responde correctamente y muestra
    # los productos disponibles para el usuario no autenticado.
    def test_listado_publico_muestra_productos(self):
        response = self.client.get(reverse('catalogo:producto_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Monitor 27')

    # Prueba que la búsqueda por nombre funcione y filtre los resultados.
    def test_busqueda_por_nombre_filtra_resultados(self):
        response = self.client.get(reverse('catalogo:producto_list'), {'q': 'Monitor'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Monitor 27')
        self.assertNotContains(response, 'No se encontraron productos')

    # Confirma que el formulario de creación está protegido por login.
    def test_creacion_requiere_login(self):
        response = self.client.get(reverse('catalogo:producto_create'))

        self.assertEqual(response.status_code, 302)

    # Valida que un usuario autenticado puede crear un producto correctamente.
    def test_usuario_autenticado_puede_crear_producto(self):
        self.client.login(username='tester', password='123456')

        response = self.client.post(
            reverse('catalogo:producto_create'),
            {
                'nombre': 'Mouse Gamer',
                'categoria': 'perifericos',
                'precio': 70000,
                'stock': 8,
                'descripcion': 'Mouse con sensor óptico.',
                'estado': True,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Producto.objects.filter(nombre='Mouse Gamer').exists())


class LoginTests(TestCase):
    # Comprueba que la autenticación con el usuario administrador funciona.
    def test_login_admin_works(self):
        user = get_user_model().objects.create_user(
            username='admin',
            password='admin123',
            is_staff=True,
            is_superuser=True,
        )

        login = self.client.login(username='admin', password='admin123')

        self.assertTrue(login)
        self.assertTrue(user.is_authenticated)
