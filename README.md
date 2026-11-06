# Refugio Huellitas (Certamen2)

Aplicación web hecha con Django para administrar un refugio de animales. Permite ver las mascotas en adopción, filtrarlas por especie y, con una cuenta, gestionar mascotas y especies según el grupo de permisos del usuario.

## Requisitos

- Python 3.10 o superior
- pip

La base de datos es SQLite (viene incluida con Python), por lo que no hay que instalar nada más.

## Instalación

### 1. Abrir una terminal en la carpeta del proyecto

Debe ser la carpeta donde está el archivo `manage.py`.

### 2. Crear y activar un entorno virtual (recomendado)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar las migraciones

```bash
python manage.py makemigrations refugio
python manage.py migrate
```

Esto crea las tablas en el archivo `db.sqlite3`.

### 5. Crear los grupos de permisos

```bash
python manage.py crear_grupos
```

Crea tres grupos:

| Grupo | Permisos |
|---|---|
| Visitantes | Solo ver el panel de gestión |
| Voluntarios | Ver, agregar y editar |
| Administradores | Ver, agregar, editar y eliminar |

### 6. Crear un superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones (nombre de usuario, correo y contraseña).

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre el navegador en http://127.0.0.1:8000/

## Uso

1. Entra a http://127.0.0.1:8000/admin/ con el superusuario.
2. En **Users**, crea los usuarios y asígnales un grupo (Visitantes, Voluntarios o Administradores).
3. Inicia sesión en http://127.0.0.1:8000/inicioSesion/.
4. Desde el **Panel de Gestión** se pueden agregar, editar y eliminar mascotas y especies, según los permisos del grupo.

Primero se debe crear al menos una **especie** y después las mascotas, porque cada mascota pertenece a una especie.

> La imagen de cada mascota se ingresa como **URL** y debe ser un enlace directo a la imagen (que termine en .jpg, .png, etc.).

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Página de inicio |
| `/mascotas/` | Lista de mascotas y filtro por especie |
| `/inicioSesion/` | Inicio de sesión |
| `/logout/` | Cerrar sesión |
| `/panelGestion/` | Panel de gestión (requiere permisos) |
| `/admin/` | Administración de Django |

## Estructura

```
Certamen2/          Configuración del proyecto (settings.py, urls.py)
refugio/            Aplicación principal
├── models.py       Modelos Mascota y Especie
├── views.py        Vistas
├── admin.py        Registro de modelos en el admin
├── templates/      Archivos HTML
├── static/css/     estilos.css
└── management/commands/crear_grupos.py
```
