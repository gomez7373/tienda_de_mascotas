# app.py
# Archivo principal para inicializar y ejecutar la aplicación Flask

from flask import Flask, render_template  # Importa Flask y render_template de Flask
from routes.user_routes import user_bp  # Importa el Blueprint de rutas de usuarios
from routes.animal_routes import animal_bp  # Importa el Blueprint de rutas de animales
import os  # Importa el módulo os para interactuar con el sistema operativo
from config import DevelopmentConfig, ProductionConfig  # Importa las configuraciones de desarrollo y producción

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar la aplicación Flask usando las variables de entorno
if os.getenv('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)  # Configuración para desarrollo
else:
    app.config.from_object(ProductionConfig)  # Configuración para producción

# Registrar los Blueprints para las rutas de usuarios y animales
app.register_blueprint(user_bp)
app.register_blueprint(animal_bp)

@app.route('/')
def index():
    """
    Ruta para la página principal.
    Renderiza la plantilla 'index.html'.
    """
    return render_template('index.html')

@app.route('/purchase')
def purchase():
    """
    Ruta para la página de compra.
    Renderiza la plantilla 'purchase.html'.
    """
    return render_template('purchase.html')

@app.route('/payment')
def payment():
    """
    Ruta para la página de pago.
    Renderiza la plantilla 'payment.html'.
    """
    return render_template('payment.html')

if __name__ == "__main__":
    # Inicia la aplicación Flask en modo debug en el puerto 5000
    app.run(debug=app.config['DEBUG'], port=5000)
