# Dockerfile
# Este archivo define la imagen Docker para la aplicación Flask.

# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos al directorio de trabajo
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la aplicación al directorio de trabajo
COPY . .

# Establece la variable de entorno para Flask
ENV FLASK_APP=app.py

# Expone el puerto 5000 para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]

