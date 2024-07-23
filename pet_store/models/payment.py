# models/payment.py
# Modelo para los pagos, define las operaciones y la estructura de los datos de los pagos

class Payment:
    def __init__(self, user_id, amount, payment_date, payment_status):
        """
        Inicializa un nuevo pago.
        :param user_id: ID del usuario que realiza el pago
        :param amount: Monto del pago
        :param payment_date: Fecha del pago
        :param payment_status: Estado del pago
        """
        self.user_id = user_id  # ID del usuario
        self.amount = amount  # Monto del pago
        self.payment_date = payment_date  # Fecha del pago
        self.payment_status = payment_status  # Estado del pago

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
        db.connection.commit()
        if json_db:
            data = self.to_dict()
            json_db.append("payments", data)

    @staticmethod
    def get_by_user(db, user_id):
        """
        Obtiene todos los pagos de un usuario específico.
        :param db: Conexión a la base de datos
        :param user_id: ID del usuario
        :return: Lista de instancias de Payment
        """
        db.cursor.execute("SELECT * FROM payments WHERE user_id = ?", (user_id,))
        rows = db.cursor.fetchall()
        return [Payment(row[1], row[2], row[3], row[4]) for row in rows]

    def to_dict(self):
        """
        Convierte la instancia de Payment a un diccionario.
        :return: Diccionario con los datos del pago
        """
        return {
            "user_id": self.user_id,
            "amount": self.amount,
            "payment_date": self.payment_date,
            "payment_status": self.payment_status
        }
