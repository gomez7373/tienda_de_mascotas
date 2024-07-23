# app.py
# Archivo principal para inicializar y ejecutar la aplicación Flask

import os
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from routes.user_routes import user_bp
from routes.animal_routes import animal_bp
from routes.payment_routes import payment_bp
from config import DevelopmentConfig
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Imprimir las variables de entorno para verificar que están cargadas correctamente
print(f"SECRET_KEY: {app.config['SECRET_KEY']}")
print(f"DATABASE_URL: {app.config['SQLALCHEMY_DATABASE_URI']}")
print(f"FLASK_ENV: {app.config['ENV']}")

# Inicializar la base de datos y las sesiones
db = SQLAlchemy(app)
Session(app)

# Registrar Blueprints
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(animal_bp, url_prefix='/animals')
app.register_blueprint(payment_bp, url_prefix='/payments')

@app.route('/')
def index():
    """
    Ruta para la página de inicio.
    """
    return render_template('index.html')

# Habilitar la ejecución de la aplicación Flask en modo debug
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
