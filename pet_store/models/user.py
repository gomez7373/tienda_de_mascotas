# models/user.py
# Modelo para el usuario, define las operaciones y la estructura de los datos del usuario

from base import check_password  # Importar la función check_password

class User:
    def __init__(self, email, password, name, surname, is_admin=False):
        """
        Inicializa un nuevo usuario.
        :param email: Email del usuario
        :param password: Contraseña del usuario (hash)
        :param name: Nombre del usuario
        :param surname: Apellido del usuario
        :param is_admin: Booleano indicando si el usuario es administrador
        """
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.is_admin = is_admin

    def save(self, db, json_db=None):
        """
        Guarda el usuario en la base de datos.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        db.cursor.execute(
            "INSERT INTO users (email, password, name, surname, is_admin) VALUES (?, ?, ?, ?, ?)",
            (self.email, self.password, self.name, self.surname, self.is_admin)
        )
        db.connection.commit()
        if json_db:
            data = self.to_dict()
            json_db.append("users", data)

    @staticmethod
    def authenticate(db, email, password):
        """
        Autentica un usuario comprobando su email y contraseña.
        :param db: Conexión a la base de datos
        :param email: Email del usuario
        :param password: Contraseña del usuario
        :return: Instancia de User si la autenticación es exitosa, None en caso contrario
        """
        db.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = db.cursor.fetchone()
        if user and check_password(user[2], password):
            return user
        return None

    @staticmethod
    def is_admin(db, email):
        """
        Verifica si un usuario es administrador.
        :param db: Conexión a la base de datos
        :param email: Email del usuario
        :return: True si el usuario es administrador, False en caso contrario
        """
        db.cursor.execute("SELECT is_admin FROM users WHERE email = ?", (email,))
        return db.cursor.fetchone()[0] == 1

    def to_dict(self):
        """
        Convierte la instancia de User a un diccionario.
        :return: Diccionario con los datos del usuario
        """
        return {
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "surname": self.surname,
            "is_admin": self.is_admin
        }
