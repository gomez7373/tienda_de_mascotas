# models/request.py
# Modelo para las solicitudes de animales, define las operaciones y la estructura de los datos de las solicitudes

class Request:
    def __init__(self, user_id, animal, phone):
        """
        Inicializa una nueva solicitud de animal.
        :param user_id: ID del usuario que realiza la solicitud
        :param animal: Nombre del animal solicitado
        :param phone: Número de teléfono del usuario
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
        # Ejecuta la consulta SQL para insertar la nueva solicitud en la base de datos
        db.cursor.execute(
            "INSERT INTO requests (user_id, animal, phone) VALUES (?, ?, ?)",
            (self.user_id, self.animal, self.phone)
        )
        db.connection.commit()  # Confirma la transacción en la base de datos

        # Si se proporciona json_db, añade la solicitud al archivo JSON
        if json_db:
            data = self.to_dict()  # Convierte la solicitud a un diccionario
            json_db.append("requests", data)  # Añade el diccionario al archivo JSON

    @staticmethod
    def get_by_user(db, user_id):
        """
        Obtiene todas las solicitudes de un usuario específico.
        :param db: Conexión a la base de datos
        :param user_id: ID del usuario
        :return: Lista de instancias de Request
        """
        # Ejecuta la consulta SQL para seleccionar todas las solicitudes del usuario
        db.cursor.execute("SELECT * FROM requests WHERE user_id = ?", (user_id,))
        rows = db.cursor.fetchall()  # Recupera todas las filas resultantes

        # Crea una lista de instancias de Request a partir de las filas recuperadas
        return [Request(row[1], row[2], row[3]) for row in rows]

    def to_dict(self):
        """
        Convierte la instancia de Request a un diccionario.
        :return: Diccionario con los datos de la solicitud
        """
        # Devuelve un diccionario con los datos de la solicitud
        return {
            "user_id": self.user_id,  # ID del usuario
            "animal": self.animal,  # Nombre del animal solicitado
            "phone": self.phone  # Número de teléfono del usuario
        }
