# TechStore INACAP

TechStore INACAP es un sistema web desarrollado en Django para gestionar un catálogo de productos tecnológicos. La aplicación permite visualizar productos, filtrarlos por categoría, buscar por nombre y revisar el detalle de cada artículo. También incluye una parte administrativa protegida por autenticación para crear, editar y eliminar productos.

## Descripción del proyecto

Este proyecto simula una tienda de tecnología con un catálogo público y un panel administrativo interno. Las funcionalidades principales están orientadas a la gestión de inventario y a la experiencia de compra del cliente.

## Funcionalidades principales

- Catálogo público con tarjetas de productos
- Búsqueda por nombre
- Filtro por categoría
- Vista detallada del producto
- CRUD completo para administración
- Login y logout de usuarios
- Navegación con menú dinámico según sesión del usuario
- Persistencia con SQLite y ORM de Django
- Diseño responsive con Bootstrap

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- Bootstrap
- Formularios de Django

## Requisitos

- Python 3.12 o superior
- Django instalado mediante requirements.txt
- Entorno virtual recomendado

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd TechStore-ev2
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

5. Ejecuta el proyecto:
   ```bash
   python manage.py runserver
   ```

6. Abre la aplicación en el navegador:
   ```text
   http://127.0.0.1:8000/
   ```

## Credenciales de prueba

El proyecto incluye un usuario administrador válido para pruebas:

- Usuario: admin
- Contraseña: admin123

Esto permite ingresar al sistema de administración y gestionar los productos desde la interfaz web.

## Objetivo del sistema

El objetivo del sistema es ofrecer una experiencia sencilla y funcional de gestión de productos tecnológicos, combinando un catálogo público con administración interna del inventario en una plataforma web desarrollada con Django.

## Estructura general

- `catalogo/`: modelo, vistas, formularios y templates del catálogo
- `techstore_project/`: configuración principal del proyecto Django
- `templates/`: templates base y de autenticación
- `db.sqlite3`: base de datos local del proyecto

## Observación

La aplicación ya está preparada para funcionar con SQLite y no requiere configuración adicional para una ejecución local básica.
