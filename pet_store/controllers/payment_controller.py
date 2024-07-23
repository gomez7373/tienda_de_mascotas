# controllers/payment_controller.py
# Controlador para manejar la lógica relacionada con los pagos

from models.payment import Payment  # Importa la clase Payment desde el módulo models.payment
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence
from datetime import datetime  # Importa el módulo datetime para manejar fechas

class PaymentController:
    def __init__(self, db: Database, json_db: JSONPersistence = None):
        """
        Inicializa el controlador de pagos con la conexión a la base de datos y opcionalmente la persistencia en JSON.
        :param db: Conexión a la base de datos
        :param json_db: (Opcional) Persistencia en JSON
        """
        self.db = db  # Almacena la conexión a la base de datos
        self.json_db = json_db  # Almacena la persistencia en JSON si se proporciona

    def make_payment(self, user_id, amount):
        """
        Realiza un pago y lo guarda en la base de datos.
        :param user_id: ID del usuario que realiza el pago
        :param amount: Monto del pago
        :return: Diccionario con los datos del pago realizado
        """
        payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        payment_status = "completado"  # Establece el estado del pago como 'completado'
        payment = Payment(user_id, amount, payment_date, payment_status)  # Crea una nueva instancia de Payment
        payment.save(self.db, self.json_db)  # Guarda el pago en la base de datos (y en JSON si se proporciona)
        return payment.to_dict()  # Devuelve un diccionario con los datos del pago realizado

    def get_payments_by_user(self, user_id):
        """
        Obtiene todos los pagos de un usuario específico.
        :param user_id: ID del usuario
        :return: Lista de diccionarios con los detalles de los pagos del usuario
        """
        payments = Payment.get_by_user(self.db, user_id)  # Obtiene todos los pagos del usuario
        return [dict(payment) for payment in payments]  # Devuelve una lista de diccionarios con los detalles de los pagos
