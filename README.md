# Django CRUD Project

Este es un proyecto CRUD (Create, Read, Update, Delete) desarrollado con Django, que permite gestionar tareas de usuarios.

## Características
- Registro e inicio de sesión de usuarios.
- Creación, visualización, actualización y eliminación de tareas.
- Marcar tareas como completadas.
- Listado de tareas activas y completadas.

## Requisitos
Asegúrate de tener instalado lo siguiente:

- Python 3.x
- Django
- Virtualenv (opcional pero recomendado)

## Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/django-crud.git
   cd django-crud
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Aplica las migraciones de la base de datos:
   ```sh
   python manage.py migrate
   ```

5. Crea un superusuario (opcional, para acceder al panel de administración):
   ```sh
   python manage.py createsuperuser
   ```

6. Inicia el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

## Uso
- Accede a `http://127.0.0.1:8000/` en tu navegador.
- Regístrate o inicia sesión para gestionar tus tareas.
- Usa las opciones disponibles para agregar, editar, completar o eliminar tareas.

## Estructura del Proyecto
```
django-crud/
│-- djangocrud/               # Configuración del proyecto
│   │-- settings.py           # Configuración principal
│-- tasks/                    # Aplicación de tareas
│   │-- models.py             # Modelo de datos
│   │-- views.py              # Lógica de negocio
│   │-- templates/            # Plantillas HTML
│-- db.sqlite3                # Base de datos SQLite
│-- manage.py                 # Script para administrar Django
```

## Tecnologías
- Django
- Bootstrap (para el diseño)
- SQLite (base de datos por defecto)




