SQLite CLI
SQLite CLI es una herramienta de línea de comandos que viene con SQLite y te permite interactuar directamente con tu base de datos.

commando:

$ sqlite3 path_to_your_database.db

Aquí tienes un breve tutorial sobre cómo usar sqlite3 para ver y manipular tu base de datos:

Paso 1: Abrir la Base de Datos
Para abrir tu base de datos con sqlite3, usa el siguiente comando en tu terminal:

bash
Copy code
sqlite3 pet_store.db
Paso 2: Comandos Básicos de sqlite3
Una vez dentro de la CLI de sqlite3, puedes usar los siguientes comandos para interactuar con tu base de datos:

Ver las Tablas:

sql
Copy code
.tables
Ver la Estructura de una Tabla:

sql
Copy code
.schema table_name
Ver el Contenido de una Tabla:

sql
Copy code
SELECT * FROM table_name;
Insertar Datos en una Tabla:

sql
Copy code
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
Actualizar Datos en una Tabla:

sql
Copy code
UPDATE table_name SET column1 = value1 WHERE condition;
Eliminar Datos de una Tabla:

sql
Copy code
DELETE FROM table_name WHERE condition;
Salir del CLI de sqlite3:

sql
Copy code
.exit
Ejemplo de Uso
Supongamos que tienes una tabla llamada users. Aquí hay algunos comandos que podrías ejecutar:

Ver todas las tablas:

sql
Copy code
.tables
Ver la estructura de la tabla users:

sql
Copy code
.schema users
Insertar un nuevo usuario:

sql
Copy code
INSERT INTO users (email, password, name, surname, is_admin) VALUES ('test@example.com', 'password123', 'John', 'Doe', 0);
Ver el contenido de la tabla users:

sql
Copy code
SELECT * FROM users;
Actualizar el nombre de un usuario:

sql
Copy code
UPDATE users SET name = 'Jane' WHERE email = 'test@example.com';
Eliminar un usuario:

sql
Copy code
DELETE FROM users WHERE email = 'test@example.com';
