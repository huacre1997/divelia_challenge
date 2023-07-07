# Divelia Challenge

Este repositorio contiene una solución al desafío Divelia.

## Tecnologías utilizadas

- Django
- Django REST Framework
- MySQL

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/huacre1997/divelia_challenge.git
```

2. Navega al directorio del proyecto:

```bash
cd divelia_challenge
```

3. Crea y activa un entorno virtual:

```bash
python3 -m venv env
source env/bin/activate
```

4. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

5. Configuración de la base de datos:

   - Asegúrate de tener MySQL instalado y configurado en tu sistema.
   - Crea una nueva base de datos en MySQL con el nombre "pets".
   - Actualiza la configuración de la base de datos en el archivo `settings.py`. Reemplaza los valores de `DATABASES` con la configuración de tu base de datos recién creada.

6. Aplica las migraciones:

```bash
python manage.py migrate
```

7. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

8. Accede a la aplicación en tu navegador web:

```
http://localhost:8000/
```

## APIs

A continuación se describen las APIs disponibles en este proyecto:

#### Registro de un nuevo usuario

Endpoint: POST `/api/v1/users/register/`

Parámetros de entrada:
- `email` (obligatorio): dirección de correo electrónico del usuario.
- `password` (obligatorio): contraseña del usuario.
- `first_name` (obligatorio): nombre del usuario.
- `last_name` (obligatorio): apellido del usuario.

Este endpoint permite registrar un nuevo usuario en el sistema.

### API de Autenticación

#### Inicio de sesión de un usuario

Endpoint: POST `/api/v1/users/login/`

Parámetros de entrada:
- `email` (obligatorio): dirección de correo electrónico del usuario registrado.
- `password` (obligatorio): contraseña del usuario registrado.

Este endpoint permite a un usuario iniciar sesión en el sistema y obtiene un token de autenticación.


### API de Pets

#### Listar todas las mascotas

Endpoint: GET `/api/v1/pets/`

Este endpoint devuelve una lista de todas las mascotas del usuario logueado.

#### Crear una nueva mascota

Endpoint: POST `/api/v1/pets/`

Parámetros de entrada:
- `name` (obligatorio): nombre de la mascota.
- `image` (opcional): imagen de la mascota.
- `short_name` (obligatorio): nombre corto de la mascota.

#### Obtener detalles de una mascota

Endpoint: GET `/api/v1/pets/{id}/`

Este endpoint devuelve los detalles de una mascota específica según su identificador `{id}`.

#### Actualizar una mascota

Endpoint: PUT `/api/v1/pets/{id}/`

Parámetros de entrada (opcionales):
- `name`: nombre de la mascota.
- `image`: imagen de la mascota.
- `short_name`: nombre corto de la mascota.

#### Eliminar una mascota

Endpoint: DELETE `/api/v1/pets/{id}/`

Este endpoint elimina una mascota específica según su identificador `{id}`.

### API de Toys

#### Listar todos los juguetes

Endpoint: GET `/api/v1/toys/`

Este endpoint devuelve una lista de todos los juguetes registrados.

#### Crear un nuevo juguete

Endpoint: POST `/api/v1/toys/`

Parámetros de entrada:
- `name` (obligatorio): nombre del juguete.
- `price` (obligatorio): precio del juguete.
- `url` (obligatorio): URL del juguete.

#### Obtener detalles de un juguete

Endpoint: GET `/api/v1/toys/{id}/`

Este endpoint devuelve los detalles de un juguete específico según su identificador `{id}`.

### API de Gifts

#### Asociar juguete a mascota

Endpoint: POST `/api/v1/gifts/create/`

Parámetros de entrada:
- `toy` (obligatorio): identificador del juguete a asociar.
- `short_name` (obligatorio): nombre corto de la mascota a la que se va a asociar el juguete.

...

**Nota**: Para acceder a las APIs de "toys", "pets" y "gifts", es necesario iniciar sesión y obtener un token de autorización. Antes de utilizar estas APIs, se debe realizar lo siguiente:

1. Iniciar sesión utilizando la API de autenticación (`/api/v1/users/login/`) y proporcionar el correo electrónico y la contraseña del usuario registrado.
2. La respuesta de la API de autenticación incluirá un Authorization Token único para el usuario.
3. Para cada solicitud a las APIs de "toys", "pets" y "gifts", se debe incluir el siguiente encabezado en la solicitud HTTP:

```
Authorization: Token {your_token_here}
```

Reemplaza `{your_token_here}` con el Authorization Token obtenido al iniciar sesión. Sin este Authorization Token válido en el encabezado de la solicitud, las solicitudes a las APIs serán rechazadas.

