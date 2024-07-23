# models/purchase.py
# Define el modelo de datos para las compras

from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence para la persistencia en archivos JSON

class Purchase:
    def __init__(self, user_id, animal, quantity, purchase_date):
        """
        Inicializa una nueva compra con los detalles proporcionados.
        :param user_id: ID del usuario que realiza la compra
        :param animal: Nombre del animal comprado
        :param quantity: Cantidad de animales comprados
        :param purchase_date: Fecha de la compra
        """
        self.user_id = user_id  # Almacena el ID del usuario
        self.animal = animal  # Almacena el nombre del animal comprado
        self.quantity = quantity  # Almacena la cantidad de animales comprados
        self.purchase_date = purchase_date  # Almacena la fecha de la compra

    def save(self, db, json_db=None):
        """
        Guarda la compra en la base de datos.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        db.cursor.execute(
            "INSERT INTO purchases (user_id, animal, quantity, purchase_date) VALUES (?, ?, ?, ?)",
            (self.user_id, self.animal, self.quantity, self.purchase_date)
        )
        db.connection.commit()  # Guardar cambios en la base de datos
        if json_db:
            json_db.append("purchases", self.to_dict())  # Guardar en JSON si se proporciona

    @staticmethod
    def get_by_user(db, user_id):
        """
        Obtiene todas las compras de un usuario específico.
        :param db: Conexión a la base de datos
        :param user_id: ID del usuario
        :return: Lista de compras realizadas por el usuario
        """
        db.cursor.execute("SELECT * FROM purchases WHERE user_id = ?", (user_id,))
        return db.cursor.fetchall()  # Obtener todas las compras del usuario

    def to_dict(self):
        """
        Convierte el objeto Purchase a un diccionario.
        :return: Diccionario con los datos de la compra
        """
        return {
            "user_id": self.user_id,  # ID del usuario que realizó la compra
            "animal": self.animal,  # Nombre del animal comprado
            "quantity": self.quantity,  # Cantidad de animales comprados
            "purchase_date": self.purchase_date  # Fecha de la compra
        }
