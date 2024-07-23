# routes/payment_routes.py
# Define las rutas para manejar las operaciones relacionadas con los pagos

from flask import Blueprint, request, jsonify  # Importa Blueprint, request y jsonify de Flask
from controllers.payment_controller import PaymentController  # Importa el controlador de pagos
from persistence.database import Database  # Importa la clase Database
from persistence.json_persistence import JSONPersistence  # Importa la clase JSONPersistence

# Crear un Blueprint para las rutas de pagos
payment_bp = Blueprint('payment_bp', __name__)

# Instanciar la base de datos y el controlador de pagos
db = Database()
json_db = JSONPersistence()
payment_controller = PaymentController(db, json_db)

@payment_bp.route('/pay', methods=['POST'])
def make_payment():
    """
    Ruta para realizar un pago.
    Espera un JSON con los campos user_id y amount.
    """
    data = request.json  # Obtener los datos JSON del request
    user_id = data['user_id']
    amount = data['amount']
    response = payment_controller.make_payment(user_id, amount)  # Realiza el pago
    return jsonify(response), 200  # Devuelve el resultado del pago y el código de estado 200 (OK)

@payment_bp.route('/payments/<int:user_id>', methods=['GET'])
def get_payments(user_id):
    """
    Ruta para obtener los pagos de un usuario específico.
    :param user_id: ID del usuario
    """
    payments = payment_controller.get_payments_by_user(user_id)  # Obtiene los pagos del usuario
    return jsonify(payments), 200  # Devuelve los pagos y el código de estado 200 (OK)
