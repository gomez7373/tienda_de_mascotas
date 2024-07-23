# base.py
# Funciones base para manejar contraseñas

import hashlib
import hmac

def hash_password(password: str) -> str:
    """
    Genera un hash seguro para una contraseña.
    :param password: La contraseña en texto plano
    :return: El hash de la contraseña
    """
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(hashed_password: str, password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con su hash.
    :param hashed_password: El hash almacenado de la contraseña
    :param password: La contraseña en texto plano
    :return: True si coinciden, False en caso contrario
    """
    return hmac.compare_digest(hashed_password, hash_password(password))
