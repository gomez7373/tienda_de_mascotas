# controllers/user_controller.py
# Controlador para manejar la lógica relacionada con los usuarios

from models.user import User
from persistence.database import Database
from persistence.json_persistence import JSONPersistence
from base import hash_password, check_password  # Asegúrate de importar check_password aquí también

class UserController:
    def __init__(self, db: Database, json_db: JSONPersistence = None):
        """
        Inicializa el controlador de usuarios con la conexión a la base de datos y opcionalmente la persistencia en JSON.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        self.db = db
        self.json_db = json_db

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
        hashed_password = hash_password(password)
        user = User(email, hashed_password, name, surname, is_admin)
        user.save(self.db, self.json_db)
        return user.to_dict()

    def authenticate_user(self, email, password):
        """
        Autentica un usuario comprobando su email y contraseña.
        :param email: Email del usuario
        :param password: Contraseña del usuario
        :return: Diccionario con los datos del usuario autenticado o None si la autenticación falla
        """
        user = User.authenticate(self.db, email, password)
        if user:
            return {
                "id": user[0],
                "email": user[1],
                "name": user[3],
                "surname": user[4],
                "is_admin": bool(user[5])
            }
        return None

    def check_admin(self, email):
        """
        Verifica si un usuario es administrador.
        :param email: Email del usuario
        :return: Booleano indicando si el usuario es administrador
        """
        return User.is_admin(self.db, email)
