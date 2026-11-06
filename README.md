# Refugio Huellitas

**Asignatura:** Taller de Lenguajes de Programación (Certamen 2)

**Estudiante:** Maximiliano Guzman

Aplicación web hecha con Django para un refugio de animales. Permite ver las mascotas en adopción, filtrarlas por especie y, iniciando sesión, gestionar mascotas y especies según los permisos del usuario.

## Instalación y Ejecución

Sigue estos pasos en la terminal para ejecutar la aplicación:

### 1. Instalación de dependencias

Instala los requerimientos necesarios leyendo el archivo `requirements.txt`:

```
pip install -r requirements.txt
```

### 2. Aplicar migraciones

Migra los cambios y modelos a la base de datos:

```
python manage.py makemigrations
python manage.py migrate
```

### 3. Levantar el servidor

Inicia el servidor de desarrollo local:

```
python manage.py runserver
```

Una vez ejecutado, abre tu navegador web e ingresa a la siguiente URL para ver la aplicación:
👉 **`http://127.0.0.1:8000/`**

## 🔐 Usuarios de Prueba para Evaluación (Roles y Permisos)

Para la demostración de la seguridad basada en roles (`@permission_required`), se han configurado los siguientes usuarios. **Nota:** Todos los usuarios comparten la misma contraseña.

* **Contraseña general:** `pruebaRoles`

### Credenciales y Niveles de Acceso:

1. **`admin`**
   * **Rol:** Superusuario (Administrador total).
   * **Acceso:** Control y permisos absolutos en la plataforma y en el panel de administración (`/admin/`).

3. **`voluntario1`**
   * **Rol:** Grupo `Voluntarios`.
   * **Acceso:** Permisos de ver, agregar y editar (`view`, `add` y `change`). No puede eliminar: no ve los botones de eliminar y, si entra a esa función, recibe `HTTP 403 Forbidden`.

4. **`visitante1`**
   * **Rol:** Grupo `Visitantes`.
   * **Acceso:** Solo puede ver el Panel de Gestión (`view`). Al intentar agregar, editar o eliminar, el sistema denegará el acceso mostrando una respuesta `HTTP 403 Forbidden`.


### Si los usuarios no existen

Crea el superusuario con `python manage.py createsuperuser`. Luego ejecuta `python manage.py shell` y pega lo siguiente:

```python
from django.contrib.auth.models import User, Group

usuarios = [
    ('administrador1', 'Administradores'),
    ('voluntario1', 'Voluntarios'),
    ('visitante1', 'Visitantes'),
    ('singrupo1', None),
]

for nombre, grupo in usuarios:
    u, _ = User.objects.get_or_create(username=nombre)
    u.set_password('tu contraseña aquí')
    u.save()
    if grupo:
        u.groups.add(Group.objects.get(name=grupo))
```

---

## 🔗 Repositorio del Proyecto

- **GitHub:** [pega aquí el enlace de tu repositorio]
