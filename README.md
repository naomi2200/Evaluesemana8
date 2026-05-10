## Gestor de Tienda Online - shopverse_api

Este proyecto es una API RESTful desarrollada con Django y Django REST Framework para la gestión de productos y proveedores en una tienda online.

### Tecnologías utilizadas
- Python 3.x
- Django 4.2
- Django REST Framework

### Instalación y ejecución
1. Clona el repositorio y navega a la carpeta del proyecto.
2. Crea y activa un entorno virtual:
	```bash
	python -m venv venv
	venv\Scripts\activate  # En Windows
	```
3. Instala dependencias:
	```bash
	pip install -r requirements.txt
	```
4. Ejecuta migraciones:
	```bash
	python manage.py makemigrations productos
	python manage.py migrate
	```
5. Crea un superusuario (opcional, para admin):
	```bash
	python manage.py createsuperuser
	```
6. Inicia el servidor:
	```bash
	python manage.py runserver
	```

### Endpoints principales

| Endpoint                | Descripción                  |
|-------------------------|------------------------------|
| `/api/productos/`       | CRUD de productos            |
| `/api/proveedores/`     | CRUD de proveedores          |

#### Ejemplos de uso (cURL)

**Listar productos:**

curl -X GET http://localhost:8000/api/productos/
![alt text](listado_productos.png)

**Crear producto:**

curl -X POST http://localhost:8000/api/productos/ 
![POST](docs/crear_producto.png )
**Buscar productos por nombre:**
curl -X GET "http://localhost:8000/api/productos/?search=Laptop"
![alt text](docs/busqueda_producto.png)

**editar_producto**
![alt text](docs/editar_producto-id.png)
**Relacion entidad2 con entidad1
![alt text](ddocs/relacion_producto.png)

Relacion de proveedor yproducto
![alt text](rdocs/elacion_producto.png)
eliminar produto con id :1
![alt text](docs/eliminar_producto.png)

**Listar proveedores:**

curl -X GET http://localhost:8000/api/proveedores/
![GET](docs/listado_proveedor.png  )

**Crear proveedor:**
curl -X POST http://localhost:8000/api/proveedores/ 
![POST](docs/crear_proveedor.png)
**Usando PATCH**
![PATCH](docs/editar_proveedor..png)
**Eliminando**
![DELETE](/docs/eliminar_proveedor.png)
### Tabla de funcionalidades


| Funcionalidad                        | Cumplimiento | Captura sugerida                      |
|--------------------------------------|--------------|---------------------------------------|
| Listado de productos                 | ✅           | screenshots/01_listado_productos.png  |
| Creación de producto                 | ✅           | screenshots/02_crear_producto.png      |
| Edición de producto                  | ✅           | screenshots/03_editar_producto.png     |
| Eliminación de producto              | ✅           | screenshots/04_eliminar_producto.png   |
| Búsqueda de productos (por nombre)   | ✅           | screenshots/05_busqueda_producto.png   |
| Relación producto-proveedor          | ✅           | screenshots/06_relacion_producto.png   |
| CRUD de proveedores                  | ✅           | screenshots/07_crud_proveedor.png      |

> **Nota:** Las capturas deben guardarse en la carpeta `screenshots/` con los nombres indicados.

### Comandos útiles

```bash
# Crear migraciones y migrar
python manage.py makemigrations productos
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Correr el servidor
python manage.py runserver

# Crear datos de prueba en el shell
python manage.py shell
```
En el shell interactivo de Django:
```python
from productos.models import Proveedor, Producto
p1 = Proveedor.objects.create(nombre="Proveedor 1", correo="proveedor1@email.com")
p2 = Proveedor.objects.create(nombre="Proveedor 2", correo="proveedor2@email.com")
prod1 = Producto.objects.create(nombre="Laptop", precio=2500.00, stock=10, proveedor=p1)
prod2 = Producto.objects.create(nombre="Mouse", precio=50.00, stock=100, proveedor=p2)
```

### Guía de commits y subida a GitHub

1. Inicializa el repositorio (si no lo hiciste):
	```bash
	git init
	git remote add origin https://github.com/usuario/tu-repo.git
	```
2. Agrega todos los archivos nuevos y cambios:
	```bash
	git add .
	```
3. Realiza commits progresivos:
	```bash
	git commit -m "Crear app productos y modelos base"
	git commit -am "Serializers y vistas para productos y proveedores"
	git commit -am "Configurar rutas y endpoints en urls.py"
	git commit -am "Actualizar settings.py y archivos de configuración"
	git commit -am "Actualizar README.md y requirements.txt"
	# (Agrega más commits según avances y cambios)
	```
4. Sube los cambios a GitHub:
	```bash
	git push -u origin main
	```

---

**Recuerda:**
- Reemplaza los archivos antiguos por los nuevos.
- Realiza migraciones y pruebas antes de grabar el video.
- Usa Postman o cURL para demostrar cada funcionalidad.
