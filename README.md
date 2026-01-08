# Backend Django - Sistema de Gestión Empresarial

API REST desarrollada con Django y Django REST Framework para la gestión integral de un sistema empresarial que incluye módulos de personas, suministros, ventas y seguimientos.

## Descripción

Sistema backend robusto diseñado para administrar operaciones empresariales completas, incluyendo:

- **Gestión de Personas**: Usuarios, clientes y proveedores
- **Gestión de Suministros**: Productos, servicios e imágenes
- **Gestión de Ventas**: Módulo para procesar transacciones comerciales
- **Gestión de Seguimientos**: Control de mantenimientos y custodias

## Características Principales

- Autenticación JWT (JSON Web Tokens)
- API RESTful con serialización de datos
- Sistema de usuarios personalizado con roles
- Gestión de productos con imágenes
- Control de mantenimientos programados
- Registro de custodias de equipos
- CORS configurado para integración frontend
- Panel de administración Django

## Tecnologías Utilizadas

- **Framework**: Django 5.2.5
- **API**: Django REST Framework
- **Autenticación**: Simple JWT
- **Base de Datos**: SQLite3 (desarrollo) / MySQL (producción)
- **CORS**: django-cors-headers
- **Python**: 3.x

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Backend_django2
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Estructura del Proyecto

```
Backend_django2/
│
├── app_1_personas/          # Módulo de gestión de personas
│   ├── models.py            # Usuarios, Clientes, Proveedores
│   ├── serializer.py        # Serializadores
│   ├── views.py             # Vistas API
│   └── urls.py              # Rutas
│
├── app_2_suministros/       # Módulo de productos y servicios
│   ├── models.py            # Productos, Servicios, Imágenes
│   ├── serializer.py        # Serializadores
│   ├── views.py             # Vistas API
│   └── urls.py              # Rutas
│
├── app_3_ventas/            # Módulo de ventas
│   ├── models.py            # Modelos de ventas
│   └── views.py             # Vistas API
│
├── app_4_seguimientos/      # Módulo de seguimientos
│   ├── models.py            # Control Mantenimiento, Custodia
│   ├── serializer.py        # Serializadores
│   ├── views.py             # Vistas API
│   └── urls.py              # Rutas
│
├── backend/                 # Configuración principal
│   ├── settings.py          # Configuración Django
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
│
├── static/                  # Archivos estáticos
├── images/                  # Almacenamiento de imágenes
├── manage.py                # Script de gestión Django
├── requirements.txt         # Dependencias del proyecto
└── db.sqlite3              # Base de datos SQLite
```

## 🔌 Endpoints API

### Base URL
```
http://127.0.0.1:8000/
```

### Módulos

#### Personas
```
/personas/          # CRUD de usuarios, clientes y proveedores
```

#### Suministros
```
/suministros/       # CRUD de productos, servicios e imágenes
```

#### Seguimientos
```
/seguimientos/      # CRUD de mantenimientos y custodias
```

#### Administración
```
/admin/            # Panel de administración Django
```

## Autenticación

El sistema utiliza JWT (JSON Web Tokens) para la autenticación. Para acceder a los endpoints protegidos:

1. Obtener token mediante login
2. Incluir el token en las peticiones:
```
Authorization: Bearer <tu-token-jwt>
```

## Modelos de Datos

### app_1_personas
- **UsuarioModel**: Sistema de usuarios con autenticación personalizada
- **ClienteModel**: Gestión de clientes
- **ProveedorModel**: Gestión de proveedores

### app_2_suministros
- **ProductoModel**: Catálogo de productos con stock
- **ImagenModel**: Imágenes de productos
- **ServicioModel**: Catálogo de servicios

### app_4_seguimientos
- **ControlMantenimientoModel**: Programación de mantenimientos
- **CustodiaModel**: Registro de custodias de equipos

## Configuración

### Variables de Entorno (Producción)

Para entorno de producción, configura las siguientes variables:

```python
# En settings.py
DEBUG = False
SECRET_KEY = 'tu-clave-secreta-segura'
ALLOWED_HOSTS = ['tu-dominio.com']

# Configuración de base de datos MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Seguridad

- SECRET_KEY configurado
- CORS configurado para orígenes permitidos
- Autenticación JWT con blacklist
- Validaciones de contraseñas
- Cambiar DEBUG a False en producción
- Configurar ALLOWED_HOSTS apropiadamente

## Testing

```bash
python manage.py test
```

## Migraciones

Crear nuevas migraciones:
```bash
python manage.py makemigrations
```

Aplicar migraciones:
```bash
python manage.py migrate
```

Ver estado de migraciones:
```bash
python manage.py showmigrations
```

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto es parte de un proyecto integrador académico.

## Autores

Proyecto desarrollado para ISAT - II Ciclo

## Soporte

Para reportar problemas o sugerencias, por favor abre un issue en el repositorio.

---

**Nota**: Este es un proyecto en desarrollo. Algunas funcionalidades pueden estar en proceso de implementación.
