# Proyecto
Proyecto de software - Corporación Universitaria Iberoamericana
Instalación

Instalar las dependencias 
Para hacer uso de la aplicación lo primero que hay que hacer es instalar FastApi en la computadora en la cual se va a ejecutar, para eso hay que hacer lo siguiente:

Abrir la consola y en la consola escribir el siguiente comando:

pip install "fastapi[all]"


Ejecución de la aplicación

1. Inicia el servidor: En la terminal, ejecuta el siguiente comando desde el directorio principal:

uvicorn main:app --reload

2. Accede a la aplicación: Abre tu navegador y dirígete a http://127.0.0.1:8000/.


Uso de la Aplicación

1. Iniciar sesión:
. Ingresa el correo y la contraseña de uno de los usuarios en users.json.
. Si las credenciales son correctas, serás redirigido a la página de check-in.

2. Realizar check-in y check-out:
. Al iniciar sesión, verás el botón de Check-in. Haz clic para registrar tu entrada.
. Una vez registrado el check-in, aparecerá el botón Check-out. Haz clic para registrar tu salida.
. Los horarios de check-in y check-out se guardarán en el archivo users.json.

3. Cerrar sesión:
. Usa el botón Cerrar sesión para salir y regresar a la página de inicio de sesión.
