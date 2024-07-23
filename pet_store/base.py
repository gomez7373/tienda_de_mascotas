# base.py
# Archivo base para funciones y configuraciones comunes utilizadas en otros archivos

import re
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

def format_date(date):
    """
    Formatea una fecha en una cadena de texto legible.
    :param date: Fecha a formatear
    :return: Fecha formateada en formato "YYYY-MM-DD HH:MM:SS"
    """
    return date.strftime("%Y-%m-%d %H:%M:%S")

def validate_email(email):
    """
    Valida un email.
    :param email: Email a validar
    :return: True si el email es válido, False en caso contrario
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """
    Valida una contraseña.
    La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula, un número y un carácter especial.
    :param password: Contraseña a validar
    :return: True si la contraseña es válida, False en caso contrario
    """
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(password_regex, password) is not None

def hash_password(password):
    """
    Genera un hash seguro de la contraseña.
    :param password: Contraseña a hashear
    :return: Hash seguro de la contraseña
    """
    return generate_password_hash(password)

def check_password(hashed_password, password):
    """
    Verifica una contraseña contra un hash.
    :param hashed_password: Hash de la contraseña
    :param password: Contraseña a verificar
    :return: True si la contraseña es válida, False en caso contrario
    """
    return check_password_hash(hashed_password, password)

# Puedes añadir más funciones y configuraciones según las necesidades de tu proyecto
