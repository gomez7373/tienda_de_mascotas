# models/payment.py
# Define el modelo de datos para los pagos

from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence para la persistencia en archivos JSON

class Payment:
    def __init__(self, user_id, amount, payment_date, payment_status):
        """
        Inicializa un nuevo pago con los detalles proporcionados.
        :param user_id: ID del usuario que realiza el pago
        :param amount: Monto del pago
        :param payment_date: Fecha del pago
        :param payment_status: Estado del pago (ej. 'completado', 'pendiente')
        """
        self.user_id = user_id  # Almacena el ID del usuario
        self.amount = amount  # Almacena el monto del pago
        self.payment_date = payment_date  # Almacena la fecha del pago
        self.payment_status = payment_status  # Almacena el estado del pago

    def save(self, db, json_db=None):
        """
        Guarda el pago en la base de datos.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        db.cursor.execute(
            "INSERT INTO payments (user_id, amount, payment_date, payment_status) VALUES (?, ?, ?, ?)",
            (self.user_id, self.amount, self.payment_date, self.payment_status)
        )
        db.connection.commit()  # Guardar cambios en la base de datos
        if json_db:
            json_db.append("payments", self.to_dict())  # Guardar en JSON si se proporciona

    @staticmethod
    def get_by_user(db, user_id):
        """
        Obtiene todos los pagos de un usuario específico.
        :param db: Conexión a la base de datos
        :param user_id: ID del usuario
        :return: Lista de pagos realizados por el usuario
        """
        db.cursor.execute("SELECT * FROM payments WHERE user_id = ?", (user_id,))
        return db.cursor.fetchall()  # Obtener todos los pagos del usuario

    def to_dict(self):
        """
        Convierte el objeto Payment a un diccionario.
        :return: Diccionario con los datos del pago
        """
        return {
            "user_id": self.user_id,  # ID del usuario que realizó el pago
            "amount": self.amount,  # Monto del pago
            "payment_date": self.payment_date,  # Fecha del pago
            "payment_status": self.payment_status  # Estado del pago
        }
