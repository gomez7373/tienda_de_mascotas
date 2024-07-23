# models/request.py
# Define el modelo de datos para las solicitudes de animales

from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence para la persistencia en archivos JSON

class Request:
    def __init__(self, user_id, animal, phone):
        """
        Inicializa una nueva solicitud de animal con los detalles proporcionados.
        :param user_id: ID del usuario que realiza la solicitud
        :param animal: Nombre del animal solicitado
        :param phone: Número de teléfono del usuario para contacto
        """
        self.user_id = user_id  # Almacena el ID del usuario
        self.animal = animal  # Almacena el nombre del animal solicitado
        self.phone = phone  # Almacena el número de teléfono del usuario

    def save(self, db, json_db=None):
        """
        Guarda la solicitud en la base de datos.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        db.cursor.execute(
            "INSERT INTO requests (user_id, animal, phone) VALUES (?, ?, ?)",
            (self.user_id, self.animal, self.phone)
        )
        db.connection.commit()  # Guardar cambios en la base de datos
        if json_db:
            json_db.append("requests", self.to_dict())  # Guardar en JSON si se proporciona

    @staticmethod
    def get_by_user(db, user_id):
        """
        Obtiene todas las solicitudes de un usuario específico.
        :param db: Conexión a la base de datos
        :param user_id: ID del usuario
        :return: Lista de solicitudes realizadas por el usuario
        """
        db.cursor.execute("SELECT * FROM requests WHERE user_id = ?", (user_id,))
        return db.cursor.fetchall()  # Obtener todas las solicitudes del usuario

    def to_dict(self):
        """
        Convierte el objeto Request a un diccionario.
        :return: Diccionario con los datos de la solicitud
        """
        return {
            "user_id": self.user_id,  # ID del usuario que realizó la solicitud
            "animal": self.animal,  # Nombre del animal solicitado
            "phone": self.phone  # Número de teléfono del usuario para contacto
        }
