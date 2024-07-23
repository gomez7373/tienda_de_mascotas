import os  # Importa el módulo os para interactuar con las variables de entorno

class Config:
    """
    Clase base de configuración.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')  # Clave secreta utilizada por Flask
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///pet_store.db')  # URL de la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilita la señalización de modificaciones de objetos

class DevelopmentConfig(Config):
    """
    Configuración específica para el entorno de desarrollo.
    """
    DEBUG = True  # Activa el modo de depuración
    ENV = 'development'  # Establece el entorno como desarrollo

class ProductionConfig(Config):
    """
    Configuración específica para el entorno de producción.
    """
    DEBUG = False  # Desactiva el modo de depuración
    ENV = 'production'  # Establece el entorno como producción
