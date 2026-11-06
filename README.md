# Fundación Patrimonio Vivo

**Asignatura:** Taller de Lenguajes de Programación (Certamen 2)

**Estudiante:** Héctor Oxacopa

## 📦 Instalación y Ejecución

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

Para la demostración de la seguridad basada en roles (`@permission_required`), se han configurado los siguientes tres usuarios. **Nota:** Todos los usuarios comparten la misma contraseña.

* **Contraseña general:** `CoquimboUnido`

### Credenciales y Niveles de Acceso:

1. **`admin`**
   * **Rol:** Superusuario (Administrador total).
   * **Acceso:** Control y permisos absolutos en la plataforma y el panel de administración.

2. **`test`**
   * **Rol:** Gestor / Editor.
   * **Acceso:** Posee permisos explícitos de lectura, adición y edición (`add` y `change`) para Lugares Patrimoniales y Categorías.

3. **`test2`**
   * **Rol:** Usuario sin permisos.
   * **Acceso:** No posee permisos especiales de gestión. Al intentar acceder a funciones de creación, edición o eliminación, el sistema denegará el acceso mostrando una respuesta `HTTP 403 Forbidden`.

---

## 🔗 Repositorio del Proyecto

- **GitHub:** https://github.com/DevManolito/CER2-OXACOPAHECTOR.git