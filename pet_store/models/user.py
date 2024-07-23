# models/user.py
# Define el modelo de datos para los usuarios

from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence para la persistencia en archivos JSON

class User:
    def __init__(self, email, password, name, surname, is_admin=False):
        """
        Inicializa un nuevo usuario con los detalles proporcionados.
        :param email: Email del usuario
        :param password: Contraseña del usuario
        :param name: Nombre del usuario
        :param surname: Apellido del usuario
        :param is_admin: Booleano indicando si el usuario es administrador (False por defecto)
        """
        self.email = email  # Almacena el email del usuario
        self.password = password  # Almacena la contraseña del usuario
        self.name = name  # Almacena el nombre del usuario
        self.surname = surname  # Almacena el apellido del usuario
        self.is_admin = is_admin  # Almacena si el usuario es administrador o no

    def save(self, db, json_db=None):
        """
        Guarda el usuario en la base de datos.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        # Ejecuta una consulta SQL para insertar los detalles del usuario en la tabla users
        db.cursor.execute(
            "INSERT INTO users (email, password, name, surname, is_admin) VALUES (?, ?, ?, ?, ?)",
            (self.email, self.password, self.name, self.surname, int(self.is_admin))
        )
        db.connection.commit()  # Guarda los cambios en la base de datos
        if json_db:
            json_db.append("users", self.to_dict())  # Si se proporciona una instancia de JSONPersistence, guarda el usuario en el archivo JSON

    @staticmethod
    def authenticate(db, email, password):
        """
        Autentica un usuario comprobando su email y contraseña.
        :param db: Conexión a la base de datos
        :param email: Email del usuario
        :param password: Contraseña del usuario
        :return: Usuario autenticado o None
        """
        # Ejecuta una consulta SQL para buscar el usuario con el email y contraseña proporcionados
        db.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = db.cursor.fetchone()  # Obtiene el primer resultado de la consulta
        return user  # Devuelve el usuario encontrado o None si no se encuentra

    @staticmethod
    def is_admin(db, email):
        """
        Verifica si un usuario es administrador.
        :param db: Conexión a la base de datos
        :param email: Email del usuario
        :return: Booleano indicando si el usuario es administrador
        """
        # Ejecuta una consulta SQL para obtener el campo is_admin del usuario con el email proporcionado
        db.cursor.execute("SELECT is_admin FROM users WHERE email = ?", (email,))
        is_admin = db.cursor.fetchone()[0]  # Obtiene el valor de is_admin
        return bool(is_admin)  # Devuelve True si es administrador, False en caso contrario

    def to_dict(self):
        """
        Convierte el objeto User a un diccionario.
        :return: Diccionario con los datos del usuario
        """
        return {
            "email": self.email,  # Email del usuario
            "password": self.password,  # Contraseña del usuario
            "name": self.name,  # Nombre del usuario
            "surname": self.surname,  # Apellido del usuario
            "is_admin": self.is_admin  # Indica si el usuario es administrador
        }

