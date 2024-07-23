# controllers/user_controller.py
# Controlador para manejar la lógica relacionada con los usuarios

from models.user import User  # Importa la clase User desde el módulo models.user
from persistence.database import Database  # Importa la clase Database desde el módulo persistence.database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence desde el módulo persistence.json_persistence
from base import hash_password, check_password  # Importa las funciones hash_password y check_password

class UserController:
    def __init__(self, db: Database, json_db: JSONPersistence = None):
        """
        Inicializa el controlador de usuarios con la conexión a la base de datos y opcionalmente la persistencia en JSON.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        self.db = db  # Almacena la conexión a la base de datos
        self.json_db = json_db  # Almacena la persistencia en JSON si se proporciona

    def create_user(self, email, password, name, surname, is_admin=False):
        """
        Crea un nuevo usuario y lo guarda en la base de datos.
        :param email: Email del usuario
        :param password: Contraseña del usuario
        :param name: Nombre del usuario
        :param surname: Apellido del usuario
        :param is_admin: Booleano indicando si el usuario es administrador (False por defecto)
        :return: Diccionario con los datos del usuario creado
        """
        hashed_password = hash_password(password)  # Hashea la contraseña antes de guardarla
        user = User(email, hashed_password, name, surname, is_admin)  # Crea una nueva instancia de User
        user.save(self.db, self.json_db)  # Guarda el usuario en la base de datos (y en JSON si se proporciona)
        return user.to_dict()  # Devuelve un diccionario con los datos del usuario creado

    def authenticate_user(self, email, password):
        """
        Autentica un usuario comprobando su email y contraseña.
        :param email: Email del usuario
        :param password: Contraseña del usuario
        :return: Diccionario con los datos del usuario autenticado o None si la autenticación falla
        """
        user = User.authenticate(self.db, email, password)  # Autentica el usuario
        if user and check_password(user[2], password):  # Verifica la contraseña hash
            return {
                "id": user[0],  # ID del usuario
                "email": user[1],  # Email del usuario
                "name": user[3],  # Nombre del usuario
                "surname": user[4],  # Apellido del usuario
                "is_admin": bool(user[5])  # Indica si el usuario es administrador
            }
        return None  # Devuelve None si la autenticación falla

    def check_admin(self, email):
        """
        Verifica si un usuario es administrador.
        :param email: Email del usuario
        :return: Booleano indicando si el usuario es administrador
        """
        return User.is_admin(self.db, email)  # Verifica si el usuario es administrador y devuelve el resultado
