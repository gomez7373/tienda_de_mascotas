Instalación de Dependencias
Para asegurarte de que todas las dependencias están instaladas, puedes ejecutar el siguiente comando:

$ pip install -r requirements.txt

# Explicación detallada aquí sobre cada una de las dependencias listadas.

Dependencias en requirements.txt

1) Flask==2.0.1

Descripción: Flask es un microframework para Python basado en Werkzeug y Jinja2. Es fácil de usar y se utiliza para desarrollar aplicaciones web.
Uso: Sirve como el framework principal para tu aplicación web.

2) Flask-SQLAlchemy==2.5.1

Descripción: Flask-SQLAlchemy es una extensión para Flask que agrega soporte para SQLAlchemy, que es un ORM (Object Relational Mapper) para bases de datos.
Uso: Facilita la interacción con la base de datos dentro de la aplicación Flask.

3) SQLAlchemy==1.4.22

Descripción: SQLAlchemy es un ORM para Python que proporciona una forma de trabajar con bases de datos usando objetos en lugar de SQL.
Uso: Maneja la persistencia y las operaciones con la base de datos.

4) python-dotenv==0.19.1

Descripción: Python-dotenv es una biblioteca que carga variables de entorno desde un archivo .env.
Uso: Permite la configuración de variables de entorno de manera segura y conveniente.

5) Werkzeug==2.0.1

Descripción: Werkzeug es una biblioteca de WSGI (Web Server Gateway Interface) que se usa como el servidor web subyacente para Flask.
Uso: Proporciona utilidades y middleware para el desarrollo de aplicaciones web.

- Explicación Ampliada de Cada Dependencia

1) Flask:

* Proporciona la estructura básica de tu aplicación web.
* Maneja las solicitudes HTTP y la ruta de las URLs.
* Integra plantillas HTML y archivos estáticos.

2) Flask-SQLAlchemy:

* Simplifica la configuración de SQLAlchemy con Flask.
* Proporciona una forma fácil de definir y manipular modelos de base de datos.
* Facilita la consulta y manipulación de datos.

3) SQLAlchemy:

* Permite mapear clases Python a tablas de base de datos.
* Proporciona una capa de abstracción sobre SQL.
* Facilita la creación, lectura, actualización y eliminación (CRUD) de registros en la base de datos.

4) python-dotenv:

* Carga automáticamente las variables de entorno definidas en un archivo .env al iniciar la aplicación.
* Facilita la gestión de configuraciones sensibles y dependientes del entorno.
* Proporciona una forma segura de manejar credenciales y configuraciones.

5) Werkzeug:

* Proporciona un servidor web de desarrollo para Flask.
* Maneja la depuración y el reenvío de errores.
* Facilita la creación de middleware personalizado para manejar solicitudes y respuestas HTTP.
